# Kỹ thuật Thêm Vị thế: Dùng Cấu trúc Đo khoảng (Measured Move) của Sóng Ngược Xu hướng để Vào Lệnh Thuận Xu hướng

Trong giao dịch thuận xu hướng (trend-following), **"thêm vị thế (scaling in)"** không phải là đuổi đỉnh một cách mù quáng. Thay vào đó, nó có nghĩa chờ thị trường trình bày cấu trúc mới trước khi vào lệnh lại một cách chính xác.
Bài viết này giới thiệu phương pháp thêm vị thế thực tế: **Dùng sóng ngược xu hướng (counter-trend leg) trên khung thời gian 1 giờ và cấu trúc đo khoảng (measured move - MM) để tìm vị trí lý tưởng cho việc thêm vị thế thuận xu hướng.**

* * *

1. Logic Chiến lược: Thuận Xu hướng Lớn, Ngược Xu hướng Nhỏ — Điểm Nhịp Vào Lệnh của Tổ chức
--------------------

Khi xu hướng trên biểu đồ ngày (daily) đã được xác lập rõ ràng, thị trường thường tạo ra đợt hồi lại (pullback) ngắn hạn trên khung thời gian nhỏ hơn.
Những "sóng ngược xu hướng" ngắn hạn này chính xác là cửa sổ nơi lực xu hướng chủ đạo tích lũy động lượng (momentum).

Điểm kết thúc sóng ngược xu hướng thường là vùng chốt lời của nhà giao dịch ngược xu hướng trước đó,
và đồng thời, nó là **điểm vào lệnh tỷ lệ thắng cao** cho lực xu hướng chủ đạo vào lại.

* * *

2. Chi tiết Thực thi: Phương pháp Bốn Bước
------------

### 1. Xác nhận Xu hướng Lớn trên Biểu đồ Ngày

*   Đầu tiên, xác định biểu đồ ngày có xu hướng rõ ràng không (ví dụ: đợt tăng lớn / đợt giảm lớn);

*   Nếu xu hướng không rõ ràng, **không dùng phương pháp này** để tránh bị mắc kẹt trong vùng giao dịch (trading range).

### 2. Xác định Sóng Ngược Xu hướng trên Khung Thời gian 1 Giờ

*   Trong xu hướng, quan sát biểu đồ 1 giờ có hiển thị **đợt dao động hồi lại ngược xu hướng chính** không;

*   Đảm bảo sóng đã hoàn chỉnh, có điểm bắt đầu rõ ràng và hội tụ tự nhiên.

### 3. Tính Mục tiêu MM (Đo khoảng - Measured Move)

*   Vẽ chiều dài sóng ngược xu hướng từ "điểm bắt đầu đến điểm kết thúc";

*   Sao chép khoảng cách đó và **chiếu về phía trước** để có mức mục tiêu MM.

*   Đây là mức nơi thị trường có thể hoàn tất đợt di chuyển ngược xu hướng và chuẩn bị tiếp tục xu hướng chính.

### 4. Thêm Vị thế Chính xác

*   **Lần thêm đầu tiên**

    : Đặt lệnh giới hạn (limit order) tại mức MM 1x;

*   **Lần thêm thứ hai**

    (tùy chọn): Đặt thêm lệnh giới hạn tại mức MM 2x;

*   Đặt cắt lỗ (stop loss) tại cuối sóng ngược xu hướng, rồi dịch thêm một tick ra ngoài để đảm bảo có vùng đệm.

* * *

3. Hiểu Bản chất: Vùng Chốt lời của Gấu là Vùng Thêm Vị thế của Bò
----------------------

*   Sau khi sóng ngược xu hướng hoàn tất, gấu thường chốt lời tại 1R hoặc 2R;

*   Hai mức này tình cờ chính xác là nơi bò có thể thêm vị thế với rủi ro thấp, thuận xu hướng;

*   **Logic thuận xu hướng không thay đổi — bạn chỉ đang chờ vị trí vào lệnh tốt hơn**.

**Nói cách khác:**

> **Nơi giao dịch của gấu kết thúc là nơi cuộc tấn công của bò bắt đầu.**

* * *



---

* * *

4. Tóm tắt
----

Khi xu hướng rõ ràng, **không đuổi tăng hoặc vội vào — chờ đợt hồi lại kết thúc rồi vào lại**,
dùng mục tiêu MM của sóng ngược xu hướng. Thêm vị thế theo cách này có cả lý luận và hỗ trợ cấu trúc.

Đây không phải "gấp đôi cược" — đây là **đòn phục kích của người giao dịch thuận xu hướng**.

* * *



Bài Đánh giá Kinh điển

[Cách Giao dịch Thuận Xu hướng: Hệ thống Giao dịch Xu hướng Dựa trên Sóng và Đảo chiều Thất bại](https://mp.weixin.qq.com/s?__biz=Mzg3OTgwODE5NQ==&mid=2247484102&idx=1&sn=fd1bf54db0b9bdda170db6a06da44407&scene=21#wechat_redirect)

[Điểm Quan trọng cho Giao dịch Thuận và Ngược Xu hướng](https://mp.weixin.qq.com/s?__biz=Mzg3OTgwODE5NQ==&mid=2247483987&idx=1&sn=1849160ca028cdd7742af5205e3c5d59&scene=21#wechat_redirect)

[Cốt lõi của Giao dịch Chính xác: Mức Quan trọng của Chỉ số và Chiến lược Khối lượng Vị thế](https://mp.weixin.qq.com/s?__biz=Mzg3OTgwODE5NQ==&mid=2247484077&idx=1&sn=79a7b3dc94c78ab6e072bf4fdc8abeed&scene=21#wechat_redirect)
