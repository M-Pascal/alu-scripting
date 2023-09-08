#!/usr/bin/env ruby
# matching sender, receiver, and file
puts ARGV[0].scan(/\[SENDER\]\[(.*?)\]\[RECEIVER\]\[(.*?)\]\[FLAGS\]\[(.*?)\]/).join
