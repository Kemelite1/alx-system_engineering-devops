#!/usr/bin/env ruby
# Find the regular expression that will match the following cases
# htb, hbtn, hbbtn and hbbbtn
puts ARGV[0].scan(/hb?t?n/).join
