import os
import sys
import re

input_hostnames = open(r"C:\Users\abc\edge_hostnames1.txt", 'r')
output_hostnames_cvs= open(r"C:\Users\abc\edge_hostnames1.cvs", 'w+')

# regex to parse out all ".*" fields 
item_regex = re.compile('"([^"]*)"')

for line in input_hostnames:
    if (line.find('+')) == -1: # skip if + separator line 
        
        # add back " " in false or true column
        line = line.replace('false','"false"')
        line = line.replace('true','"true"')
        
        # find all groups out with ".*"
        match = item_regex.findall(line)
        
        # form newline for output
        newline=""
        #print(match)
        for i in range(len(match)):
            if i < len(match)-1:
              #print(match[i])
              newline += match[i]  # add groups with comma separators 
              newline += ","
            else:   # add \n if last match 
              newline += match[i]
              newline += "\n"

        #print(newline)
        output_hostnames_cvs.write(newline) # write out the groups into newline in cvs output file
        
        ''' simple code to convert Akamai edge hostnames text table to a cvs file.

inputs - a text file like below format
D:\Akamai\CLI\akamai_pipeline>akamai property-manager leh -c "ctr_1-123456" -g "grp_123456"
╒═════════════╤═══════════════════════════════════════════════╤═══════════════╤═════════════════════╤════════╤═════════════════════════════════════════════════════════════╕
│"ID"         │"Prefix"                                       │"Suffix"       │"IP Version Behavior"│"Secure"│"EdgeHostname Domain"                                        │
╞═════════════╪═══════════════════════════════════════════════╪═══════════════╪═════════════════════╪════════╪═════════════════════════════════════════════════════════════╡
│"ehn_1234"   │"abc.def.com"                                  │"edgesuite.net"│"IPV4"               │false   │"abc.def.com.edgesuite.net"                                  │
├─────────────┼───────────────────────────────────────────────┼───────────────┼─────────────────────┼────────┼─────────────────────────────────────────────────────────────┤
│"ehn_12345"  │"xyz.def.com"                                  │"edgesuite.net"│"IPV4"               │false   │"xyz.def.com.edgesuite.net"                                  │
....

first save it into ascii encoding because it may contain utf-8 encoding, then it will look like below,

+═════════════╤═══════════════════════════════════════════════╤═══════════════╤═════════════════════╤════════╤═════════════════════════════════════════════════════════════╕
│"ID"         │"Prefix"                                       │"Suffix"       │"IP Version Behavior"│"Secure"│"EdgeHostname Domain"                                        │
+═════════════╪═══════════════════════════════════════════════╪═══════════════╪═════════════════════╪════════╪═════════════════════════════════════════════════════════════╡
│"ehn_1234"   │"abc.def.com"                                  │"edgesuite.net"│"IPV4"               │false   │"abc.def.com.edgesuite.net"                                  │
+─────────────┼───────────────────────────────────────────────┼───────────────┼─────────────────────┼────────┼─────────────────────────────────────────────────────────────┤
│"ehn_12345"  │"xyz.def.com"                                  │"edgesuite.net"│"IPV4"               │false   │"xyz.def.com.edgesuite.net"                                  │
....

outputs - all cvs comma separated so others can use Excel
'''
