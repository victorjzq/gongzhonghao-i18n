#!/usr/bin/env python3
import os
import sys
import argparse
import glob
import re
import requests
import json

GRAPHQL_URL = 'https://api.hashnode.com'
MUTATION = '''
mutation($publicationId: String!, $title: String!, $bodyMarkdown: String!, $tags: [String!]) {
  createPublicationPost(input: {
    publicationId: $publicationId
    title: $title
    bodyMarkdown: $bodyMarkdown
    tags: $tags
    isDraft: false
  }) {
    post {
      id
      slug
      url
    }
    success
  }
}
'''

def publish_article(file_path, publication_id, tags, dry_run):
    token = os.getenv('HASHNODE_TOKEN')
    if not token:
        print('ERROR: Set export HASHNODE_TOKEN=your_token')
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        body = f.read()
    
    # Extract title from # Title
    title_match = re.match(r'^#\s*(.+?)\s*\n', body, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else os.path.basename(file_path).replace('.md', '')
    
    variables = {
        'publicationId': publication_id,
        'title': title,
        'bodyMarkdown': body,
        'tags': tags
    }
    
    if dry_run:
        print(f'DRY-RUN: Would publish "{title}" from {file_path}')
        return True
    
    headers = {'Authorization': token}
    response = requests.post(GRAPHQL_URL, json={'query': MUTATION, 'variables': variables}, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        result = data.get('data', {}).get('createPublicationPost')
        if result and result.get('success'):
            post = result['post']
            print(f'✅ Published: {title}')
            print(f'   URL: https://yourpub.hashnode.dev/{post["slug"]}')
            print(f'   ID: {post["id"]}')
            return True
        else:
            print(f'❌ API Error: {json.dumps(data, indent=2)}')
            return False
    else:
        print(f'❌ HTTP {response.status_code}: {response.text}')
        return False

def main():
    parser = argparse.ArgumentParser(description='Batch publish Markdown to HashNode Publication')
    parser.add_argument('--dir', '-d', default='./translated/', help='Directory of .md files (default: ./translated/)')
    parser.add_argument('--publication-id', '-p', required=True, help='HashNode Publication ID (e.g. pub_XXX)')
    parser.add_argument('--tags', '-t', nargs='*', default=[], help='Tags (repeatable)')
    parser.add_argument('--dry-run', action='store_true', help='Simulate without publishing')
    
    args = parser.parse_args()
    
    md_files = glob.glob(os.path.join(args.dir, '*.md'))
    if not md_files:
        print(f'No .md files in {args.dir}')
        sys.exit(1)
    
    print(f'Found {len(md_files)} articles in {args.dir}')
    
    success_count = 0
    for file_path in md_files:
        if publish_article(file_path, args.publication_id, args.tags, args.dry_run):
            success_count += 1
    
    print(f'\nSummary: {success_count}/{len(md_files)} published')

if __name__ == '__main__':
    main()
