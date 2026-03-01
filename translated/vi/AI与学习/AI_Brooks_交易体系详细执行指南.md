# Hướng dẫn thực thi chi tiết hệ thống giao dịch Al Brooks

###

* * *

**I. Phân tích thị trường: Xác định cấu trúc thị trường**
-----------------

**Nhiệm vụ**: Xác định trạng thái thị trường hiện tại và quyết định chiến lược giao dịch.

### **1\. Xác định trạng thái thị trường hiện tại**

1.  **Xu hướng (Trend)**


*   **Xu hướng tăng (Bull Trend)**

    : Đỉnh cao hơn (HH) + Đáy cao hơn (HL).

*   **Xu hướng giảm (Bear Trend)**

    : Đỉnh thấp hơn (LH) + Đáy thấp hơn (LL).

*   **Kênh hẹp (Tight Channel)**

    : Xu hướng gần như không có hồi lại (pullback).

*   **Kênh rộng (Broad Channel)**

    : Hồi lại lớn, nhưng xu hướng tổng thể vẫn giữ nguyên.


3.  **Vùng giao dịch (Trading Range - TR)**


*   Giá di chuyển **ngang** trong một khoảng thời gian, với đỉnh và đáy nằm trong một phạm vi nhất định.

*   **Áp dụng chiến lược Mua thấp, Bán cao (BLSHS)**

    , 80% xác suất không phá vỡ.


5.  **Phá vỡ (Breakout - BO)**


*   **Phá vỡ mạnh (Strong BO)**

    : Một đợt di chuyển lớn lên/xuống phá qua, có nến theo sau (Follow-through Bar).

*   **Phá vỡ thất bại (Failed BO)**

    : Giá nhanh chóng đảo chiều sau phá vỡ và quay lại vùng giao dịch.


* * *

**II. Chiến lược giao dịch: Cách vào lệnh?**
----------------

> **Mục tiêu**: Xác định điểm vào lệnh, tín hiệu kích hoạt và mức cắt lỗ.

### **1\. Các phương pháp vào lệnh chính**

Loại giao dịch

Tín hiệu vào lệnh

Phương pháp thực thi

Cắt lỗ

Thị trường áp dụng

**Giao dịch phá vỡ (BO Trade)**

Phá vỡ mạnh + nến theo sau

Mua trên điểm phá vỡ

Dưới đáy hồi lại gần nhất

Đầu xu hướng

**Giao dịch hồi lại (PB Trade)**

Hồi lại đến đường trung bình động / hỗ trợ

Mua sau khi xác nhận bật lại

Dưới đáy hồi lại

Trong xu hướng tiếp diễn

**Giao dịch vùng giao dịch (TR Trade)**

Mua thấp, bán cao

Mua khi chạm hỗ trợ

Dưới đáy vùng giao dịch

Vùng giao dịch

**Giao dịch đảo chiều**

Kháng cự chính + mô hình đảo chiều

Mua sau khi xác nhận nến đảo chiều

Dưới đáy nến đảo chiều

Khi xu hướng đang suy yếu

* * *

### **2\. Chi tiết vào lệnh**

> **Nguyên tắc cốt lõi: Chờ nến tín hiệu + nến xác nhận để đảm bảo phá vỡ hoặc hồi lại thành công!**

#### **(1) Giao dịch phá vỡ (BO)**

**Các bước thực thi**:

1.  Quan sát xem thị trường có đang ở **Chế độ phá vỡ** không:


*   Giá đã ở trong vùng giao dịch **hơn 20 nến**.

*   Giá gần kháng cự/hỗ trợ và thể hiện ý định phá vỡ (nến lớn).


3.  Xác định **Nến phá vỡ**:


*   **Thân nến lớn**

    , bóng nến trên/dưới ngắn, đóng cửa gần đỉnh/đáy.

*   **Khối lượng tăng**

    , cho thấy dòng vốn chảy vào.


5.  **Xác nhận phá vỡ**

*   **Sau nến phá vỡ, nến theo sau phải tiếp tục cùng hướng**

    .

*   Nếu nến thứ hai hồi lại quá sâu, có thể là phá vỡ thất bại.


7.  **Thực thi vào lệnh**

*   **Mua (Long)**

    : Đặt lệnh trên giá đóng cửa nến phá vỡ + trên mức kháng cự.

*   **Bán (Short)**

    : Đặt lệnh dưới giá đóng cửa nến phá vỡ + dưới mức hỗ trợ.


9.  **Cắt lỗ**

*   **Đặt cắt lỗ dưới đáy nến phá vỡ hoặc dưới mức hồi lại gần nhất**

    .




* * *

#### **(2) Giao dịch hồi lại (PB Trade)**

**Các bước thực thi**:

1.  **Xu hướng đã xác lập**

    :


*   Đảm bảo thị trường đã hình thành xu hướng rõ ràng (đỉnh và đáy tạo mô hình bậc thang).

*   Xác định các mức hỗ trợ chính (như **EMA20, đỉnh trước, đáy trước**).


3.  **Xác nhận hồi lại**

    :


*   **Nến tín hiệu bò (bull)**

    : Bóng nến dưới dài, thân nến đóng cửa cao.

*   **Nến tín hiệu gấu (bear)**

    : Bóng nến trên dài, thân nến đóng cửa thấp.


*   Quan sát giá hồi lại trong **3-5 nến**.

*   **Bóng nến dài trên nến hồi lại cho thấy sự can thiệp của người mua/bán**

    .

*   **Xuất hiện nến tín hiệu**

    :


6.  **Vào lệnh**

*   **Mua (Long)**

    : Vào lệnh 1 tick trên đỉnh nến tín hiệu.

*   **Bán (Short)**

    : Vào lệnh 1 tick dưới đáy nến tín hiệu.


8.  **Cắt lỗ**

*   **Đặt cắt lỗ dưới đáy nến tín hiệu hoặc dưới mức hỗ trợ**

    .




* * *

**III. Quản lý rủi ro: Cách kiểm soát thua lỗ?**
------------------

> **Mục tiêu**: Giới hạn thua lỗ tối đa mỗi giao dịch ở mức 1%-2% vốn tài khoản.

### **1\. Quản lý vốn**

*   Rủi ro mỗi giao dịch **≤ 2% tổng vốn tài khoản**.

*   **Giới hạn thua lỗ hàng ngày tối đa = 4-6% tài khoản**

    , **ngừng giao dịch** sau khi vượt giới hạn thua lỗ hàng ngày.


### **2\. Chiến lược cắt lỗ**

Loại giao dịch

Chiến lược cắt lỗ

**Giao dịch phá vỡ (BO Trade)**

Cắt lỗ tại **đáy nến phá vỡ**

**Giao dịch hồi lại (PB Trade)**

Cắt lỗ tại **đáy hồi lại (HL) hoặc đỉnh (LH)**

**Giao dịch vùng giao dịch (TR Trade)**

Cắt lỗ tại **2-3 tick ngoài phạm vi**

**Giao dịch đảo chiều**

Cắt lỗ tại **đáy/đỉnh nến đảo chiều**

### **3\. Chiến lược chốt lời**

Loại giao dịch

Chiến lược chốt lời

**Giao dịch xu hướng**

**2 lần rủi ro**

 hoặc **Mục tiêu Measured Move**

**Giao dịch hồi lại (PB Trade)**

**Chốt lời một phần tại đỉnh/đáy trước**

, giữ vị thế còn lại

**Giao dịch vùng giao dịch (TR Trade)**

**Chốt lời tại đỉnh/đáy vùng giao dịch**

**Giao dịch đảo chiều**

**Chốt lời tại đỉnh/đáy trước**

* * *

* * *

**Tóm tắt**
------

1.  **Xác nhận trạng thái thị trường (xu hướng / vùng giao dịch / phá vỡ)**

    .

2.  **Chờ tín hiệu vào lệnh phù hợp (nến phá vỡ / nến hồi lại / nến tín hiệu)**

    .

3.  **Đặt mức cắt lỗ và chốt lời hợp lý (2 lần rủi ro / mục tiêu measured move)**

    .

4.  **Tuân thủ nghiêm ngặt quản lý rủi ro (rủi ro mỗi giao dịch ≤ 2%)**

    .

5.  **Đánh giá lại và tối ưu chiến lược giao dịch để cải thiện tỷ lệ thắng và tỷ lệ rủi ro/lợi nhuận**

    .
