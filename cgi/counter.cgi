#!/usr/bin/perl

open(IN, "count.dat");
$count = <IN>;
close(IN);

$count++;

open(OUT, "> count.dat");
print OUT $count;
close(OUT);

@array = split(//, $count);
for ($i=0; $i<= $#array; $i++) {
    print("<img src\"=\\img\\num\\$array[$i].gif\">");
}
