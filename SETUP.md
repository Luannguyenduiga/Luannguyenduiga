# Cài profile GitHub

Bộ profile này dành cho **Luannguyenduiga**. Nội dung lấy từ portfolio hiện có; GIF pixel được vẽ riêng bằng script trong thư mục `tools`.

1. Mở https://github.com/new và tạo repository **Public** tên chính xác là `Luannguyenduiga` trong tài khoản của bạn. Nếu repo này đã có, dùng repo hiện tại.
2. Chép **nội dung bên trong** thư mục `github-profile` vào gốc repo đó. Cấu trúc tối thiểu:

   ```text
   Luannguyenduiga/
   ├── README.md
   └── assets/
       └── pixel-code.gif
   ```

3. Commit lên nhánh mặc định rồi mở https://github.com/Luannguyenduiga để xem profile.

Chỉ dán README mà không tải thư mục `assets` lên sẽ làm GIF bị thiếu. Không đặt cả thư mục `github-profile` thành thư mục con trong repo profile.

## Chỉnh sửa

- Nội dung, tech stack, liên hệ, dự án và URL stats đều nằm trong `README.md`.
- Tạo lại GIF: cài Python và Pillow (`python -m pip install Pillow`), rồi chạy `python tools/render_banner.py` từ thư mục này. Script dùng font bitmap có sẵn của Pillow, không cần tải font.
- GIF là hoạt ảnh minh họa vòng lặp code và trạng thái build; không phải dữ liệu chạy thật. GitHub stats và streak lấy dữ liệu từ dịch vụ bên ngoài, có thể bị cache, giới hạn lượt gọi hoặc tạm lỗi. Nếu card không hiện, thử mở trực tiếp URL của ảnh sau vài phút. Không cần token cho cấu hình công khai này.
- Các badge và icon cũng cần kết nối đến dịch vụ bên ngoài; chữ giới thiệu và GIF vẫn nằm trong repo của bạn.

## Tham khảo

- Bố cục giới thiệu / tech stack / stats tham khảo profile mentor: https://github.com/anhphucDao
- Quy tắc hiển thị README: https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme
- Stats: https://github.com/vn7n24fzkq/github-profile-summary-cards
- Streak: https://github.com/DenverCoder1/github-readme-streak-stats

Bộ file này được chuẩn bị trong workspace, chưa được đăng lên GitHub.
