open Core

let result = In_channel.read_lines "bin/input.txt"

let rec group input result =
  match input with
  | [] -> result
  | "" :: rest -> group rest (0 :: result)
  | cals :: rest ->
      group rest
        (match result with
        | [] -> [ int_of_string cals ]
        | hd :: tail -> (hd + int_of_string cals) :: tail)

(* Part 1 *)

let rec max_of_list input cur =
  match input with [] -> cur | hd :: rest -> max_of_list rest (max hd cur)

(* let () = print_endline (string_of_int (max_of_list (group result []) 0)) *)
let () = printf "Part 1: %d\n" (max_of_list (group result []) 0)

(* Part 2 *)

let rec max3 input (m1, m2, m3) =
  match input with
  | [] -> (m1, m2, m3)
  | hd :: rest ->
      max3 rest
        (match (m1, m2, m3) with
        | m1, m2, _ when hd > m1 -> (hd, m1, m2)
        | m1, m2, _ when hd > m2 -> (m1, hd, m2)
        | m1, m2, m3 when hd > m3 -> (m1, m2, hd)
        | _ -> (m1, m2, m3))

let () =
  let m1, m2, m3 = max3 (group result []) (0, 0, 0) in
  printf "Part 2: %d\n" (m1 + m2 + m3)

(* Primeagen Part 1 - start @ 28:23 *)
