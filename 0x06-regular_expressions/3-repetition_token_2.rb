#!/usr/bin/env ruby
# hbn, hbtn, hbttn, hbtttn, hbttttn
# Find the regular expression that will match the above cases
puts ARGV[0].scan(/hbt+n/).join
