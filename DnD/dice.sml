
fun split(s : string) =
let
  val f = fn (a, b::bs) => case a of #" " => []::b::bs | s => (s::b)::bs
in
  map implode (foldr f [[]] (explode s))
end

fun listen(r : Random.rand) =
(let
  val SOME(s) = TextIO.inputLine TextIO.stdIn
  val l = split(s)
in
  (map (print o (fn x => x ^ "\n")) l; listen(r))
end) handle Bind => ()


