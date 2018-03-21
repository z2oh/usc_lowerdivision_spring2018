#!/bin/perl

use strict;
use warnings;

my @nums = split(/\s/, <STDIN>);
print("$nums[0]");
for (my $i=2; $i <= $#nums; $i++)
{
	print("-${\($nums[$i]-1)},${\($nums[$i]+1)}");
}
print("-$nums[1]\n");
