#!/usr/bin/env ruby
# matching sender, receiver, and file
puts ARGV[0].scan((?<=[a-z]:)(?<group>\S+\w)/)[0, 3].join(',')
