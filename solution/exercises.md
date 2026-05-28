# Ngày 1 — Bài Tập & Phản Ánh
## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ  
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 — Lập Trình Cốt Lõi (0:00–1:00)

Chạy các ví dụ trong Google Colab tại: https://colab.research.google.com/drive/172zCiXpLr1FEXMRCAbmZoqTrKiSkUERm?usp=sharing

Triển khai tất cả TODO trong `template.py`. Chạy `pytest tests/` để kiểm tra tiến độ.

**Điểm kiểm tra:** Sau khi hoàn thành 4 nhiệm vụ, chạy:
```bash
python template.py
```
Bạn sẽ thấy output so sánh phản hồi của GPT-4o và GPT-4o-mini.

---

## Phần 2 — Bài Tập Mở Rộng (1:00–1:30)

### Bài tập 2.1 — Độ Nhạy Của Temperature
Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> *Câu trả lời của bạn*

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> *Câu trả lời của bạn*

---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token.

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> *16.7 lần*


**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> 1.trường hợp chi phí cao hơn của GPT-4o là xứng đáng:
 Bối cảnh: Các tác vụ yêu cầu khả năng suy luận phức tạp, phân tích đa phương thức (multimodal như hình ảnh, biểu đồ) hoặc đòi hỏi độ chính xác tuyệt đối.
 Ví dụ cụ thể: Hệ thống hỗ trợ chẩn đoán y tế, phân tích báo cáo tài chính chuyên sâu, lập trình/sửa lỗi các kiến trúc mã nguồn phức tạp, hoặc chatbot tư vấn pháp lý. Trong các trường hợp này, một sai sót nhỏ có thể gây thiệt hại lớn, nên việc trả chi phí cao để đổi lấy chất lượng và độ chính xác của GPT-4o là hoàn toàn xứng đáng. 2. Trường hợp GPT-4o-mini là lựa chọn tốt hơn:
 Bối cảnh: Các tác vụ có khối lượng dữ liệu lớn (high volume), lặp đi lặp lại, yêu cầu tốc độ xử lý nhanh và không đòi hỏi tư duy quá sâu chuỗi.
 Ví dụ cụ thể: Chatbot chăm sóc khách hàng trả lời các câu hỏi thường gặp (FAQs), hệ thống phân loại sắc thái bình luận (Sentiment Analysis) trên mạng xã hội, tóm tắt văn bản ngắn, hoặc trích xuất thông tin cơ bản từ email. Sử dụng GPT-4o-mini giúp tối ưu hóa chi phí vận hành lên tới hàng chục lần mà vẫn đảm bảo hiệu suất công việc*

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> treaming quan trọng nhất trong các ứng dụng dịch vụ tương tác trực tiếp với con người (như Chatbot AI, trợ lý ảo), nơi Thời gian phản hồi đầu tiên (Time to First Token - TTFT) quyết định trải nghiệm người dùng. Việc hiển thị văn bản ngay khi nó vừa được tạo ra giúp người dùng có cảm giác hệ thống đang phản hồi ngay lập tức, giảm tâm lý chờ đợi ức chế.
Ngược lại, Non-streaming sẽ tốt hơn trong các tác vụ xử lý ngầm (background jobs) hoặc khi kết quả đầu ra được tiêu thụ bởi một hệ thống/phần mềm khác thay vì con người. Ví dụ như khi cần trích xuất dữ liệu định dạng JSON để đưa vào database, tạo báo cáo tự động, hoặc phân tích cú pháp mã nguồn; lúc này, việc đợi toàn bộ phản hồi hoàn thành để đảm bảo tính toàn vẹn của dữ liệu quan trọng hơn là tốc độ hiển thị từng từ.


## Danh Sách Kiểm Tra Nộp Bài
- [ ] Tất cả tests pass: `pytest tests/ -v`
- [ ] `call_openai` đã triển khai và kiểm thử
- [ ] `call_openai_mini` đã triển khai và kiểm thử
- [ ] `compare_models` đã triển khai và kiểm thử
- [ ] `streaming_chatbot` đã triển khai và kiểm thử
- [ ] `retry_with_backoff` đã triển khai và kiểm thử
- [ ] `batch_compare` đã triển khai và kiểm thử
- [ ] `format_comparison_table` đã triển khai và kiểm thử
- [ ] `exercises.md` đã điền đầy đủ
- [ ] Sao chép bài làm vào folder `solution` và đặt tên theo quy định 
