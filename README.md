8 Rooks – (Thuật toán tìm kiếm cho “8 con xe”)

Vấn đề của đặt 8 quân xe (Rook) trên bàn cờ 8×8 sao cho không con nào ăn nhau tức là chúng không nằm trên cùng 1 hàng, cột. 
1) Mô hình hoá bài toán

Trạng thái (state): ma trận nhị phân 8×8, 1 là có xe, 0 là trống.

Trạng thái đầu: bàn cờ trống hoặc trạng thái có xe rôi tùy thuộc riêng vào từng loại thuật toán.

Đích (goal): đúng 8 xe, mỗi hàng tối đa 1 xe, mỗi cột tối đa 1 xe hoặc theo môt bàn cờ ta cho hợp lệ

Hàm chi phí:

Với các thuật toán chi phí đồng nhất: mỗi bước = 1.

Với heuristic (Greedy, A*): dùng hàm đánh giá dựa trên độ lệch cột trong cùng hàng đã có so với mục tiêu

2) Các thuật toán
2.1. BFS (Breadth-First Search)
Chiến lược: duyệt theo lớp mở rộng tất cả trạng thái ở độ sâu d (đã đặt d xe) rồi mới sang d+1.
Trong 8 quân xe: với cách sinh “điền từng hàng”, BFS sẽ lần lượt xét mọi cách đặt hợp lệ cho hàng 0, xong đến hàng 1, … cho đến khi đủ 8 hàng. Muốn chắc chắn ra nghiệm ngắn nhất và chấp nhận tiêu tốn bộ nhớ.

2.2. DFS (Depth-First Search)

Chiến lược: đi sâu một nhánh (đặt liên tiếp xuống các hàng 0→1→…→7). Nếu kẹt (không còn cột hợp lệ), quay lui: đổi cột ở hàng gần nhất còn lựa chọn, rồi tiếp tục đi sâu lại. Dễ đi lạc vào nhánh xấu (đến hàng sâu mới phát hiện bế tắc) → mất thời gian quay lui.
Không đảm bảo nếu có nhiều nghiệm (gặp nghiệm nào trước thì dừng).


2.3. UCS (Uniform-Cost Search)

Chiến lược: luôn mở rộng trạng thái có tổng chi phí đường đi nhỏ nhất (priority queue).
UCS không dùng heuristic như các nhóm khác; nó chỉ xét chi phí thực đã đi (g(n)).
Trong 8 quân xe
Nếu mỗi đặt xe = 1 như bài em, UCS giống BFS 
Khi bạn thực sự có chi phí bước khác nhau; còn nếu mọi bước = 1, chọn BFS cho gọn.

2.4. DLS (Depth-Limited Search)
Chiến lược: DFS nhưng giới hạn độ sâu.
Trong 8 quân xe: nghiệm có độ sâu đúng bằng 8 (đặt đủ 8 xe). Đặt limit = 8 là hợp lý.
Nếu đặt quá nhỏ thì không ra nghiệm 8 quân xe thì nên để độ sâu bằng 8

2.5. IDS (Iterative Deepening Search)

Chiến lược: chạy DLS với limit = 0, 1, 2, … tăng dần cho đến khi gặp nghiệm. Trong 8 quân xe  Hoàn chỉnh như BFS, bộ nhớ như DFS.
Với nghiệm sâu 8, IDS sẽ thử 0→1→…→8. Chi phí lặp lại ở tầng nông là chấp nhận được vì không gian nhỏ.
Khi nên dùng: muốn sự cân bằng giữa tối ưu (số bước) và bộ nhớ thấp.

2.6. Greedy Best-First Search
Chiến lược: mở rộng trạng thái có heuristic h nhỏ nhất (không tính g).
Heuristic trong code: thiên về “gom hàng”: nếu đã có xe cùng hàng, chọn cột gần nhau (độ lệch cột nhỏ) → ưu tiên những bố cục “gọn”.
Trong 8 quân xe không đảm bảo tối ưu nhưng có thể nhanh

2.7. A* 
Chiến lược: ưu tiên f(n) = g(n) + h(n)
g(n): số xe đã đặt (chi phí thật).
h(n): heuristic như Greedy.
Trong 8 quân xe
Nếu h chấp nhận (không “quá lạc quan”), A* tối ưu theo số bước. Nhanh hơn BFS khi h dẫn đường tốt, nhưng tốn bộ nhớ hơn Greedy do giữ nhiều node “tiềm năng”.

2.8. Beam Search
Chiến lược: Best-First cắt tỉa mạnh — mỗi lớp chỉ giữ K ứng viên tốt nhất (beam width).
Trong 8 quân xe
Rất nhanh và tiết kiệm bộ nhớ khi chọn K nhỏ (ví dụ 3).
Dễ bỏ lỡ nghiệm nếu ở lớp nào đó nghiệm “nằm ngoài” K tốt nhất bị loại sớm.


2.9. Backtracking (Quay lui)

Cách làm đúng với 8 quân xe: đặt theo từng hàng; mỗi khi chọn cột gây xung đột (trùng cột với hàng trước), quay lui đổi cột ở hàng đó; nếu hết cột → lùi lên hàng trên.
Có ràng buộc đơn giản như không trùng hàng/cột; kết hợp thứ tự hóa cột tốt sẽ rất nhanh.
Nếu thứ tự thử cột “xấu” do random, thời gian tăng đáng kể (nhưng vẫn nhẹ bộ nhớ).

2.10. Forward Checking (FWCK)

Ý tưởng: mỗi lần đặt một xe, cắt miền giá trị của các hàng sau
Gỡ bỏ mọi cột đã bị chiếm, và những ô gây xung đột theo ràng buộc.
Trong 8 quân xe: vì ràng buộc chỉ là “không trùng cột”, cắt miền làm giảm rất rõ nhánh thử, thường nhanh hơn backtracking mù.

2.11. Mù một phần / Mù toàn phần
Mô phỏng “tập các bàn cờ” cùng lúc: áp dụng chung một hành động lên tất cả ma trận trong tập, kiểm tra điều kiện “tập con/siêu tập” để dừng.

2.12. AND-OR Search
Khi có mục tiêu phân rã: nút OR (chọn một cách đặt), nút AND (phải thỏa đồng thời nhiều ràng buộc).
Trong 8 quân xe: dùng để biểu diễn kế hoạch đặt lần lượt, kèm các ràng buộc “phải đúng cả hàng lẫn cột”. Tính thực dụng thấp hơn so với BFS/IDS/A* cho bài toán này, nhưng hữu ích về mặt khái niệm.
2.13. Genetic Algorithm (GA) — nói riêng cho 8 quân xe, tập trung nhược điểm
Biểu diễn & ràng buộc khó:
Dùng ma trận nhị phân hoặc mã hóa “mỗi hàng một cột” vẫn dễ sinh cấu hình vi phạm (trùng cột). Cần toán tử lai/đột biến có ý thức ràng buộc hoặc hàm sửa (repair) → phức tạp.
Fitness “đánh giá gần đúng”:
Các thước đo như “số cặp xung đột” hay “số cột trùng” thường tạo nhiều cao nguyên (plateau) và bẫy cục bộ → quần thể dậm chân hoặc hội tụ sớm.
Không có đảm bảo:
GA không cam kết tìm nghiệm, càng không đảm bảo tối ưu số bước (điều vốn đơn giản = 8 với tìm kiếm có hướng).

4) Trực quan hoá & cách chạy

Tkinter: menu nhóm thuật toán; bấm nút để chạy.

Pygame: hiển thị bảng trái (đường đi) và bảng phải (mục tiêu). Có hiệu ứng âm thanh (tieng_co.mp3) và tạm dừng mỗi bước để quan sát.

