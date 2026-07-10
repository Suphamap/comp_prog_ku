program HelloWorld;

var
  u, f, a: Integer; // 1. Declared the variables and their types

begin
  u := 5;           // 2. Changed '=' to ':=' and added semicolons
  f := 3;
  a := u + f;

  writeln('Hello, World!');
  writeln('Pascal is officially running on your Mac.');
  writeln('The sum is: ', a); // Added this to display your calculation!

  for u := 1 to 5 do
    writeln('Loop iteration: ', u);
end.