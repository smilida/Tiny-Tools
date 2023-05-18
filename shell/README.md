## Collection of basic commands
```bash
# compression
tar -zcvf example.tar.gz PATH/
# unzip
tar -zxvf example.tar.gz
tar -jxvf example.tar.bz2
tar -xf example.tar.xz

# create a screen
screen -S example
# check the list of screen
screen -ls
# recover screen
screen -r example_id
# kill screen
screen -S example_id -X quit

# count the number of specific characters in a file
grep -c "balabala" filename

# spilt string use cut
echo "string.before.dot.after" | cut -d "." 1

# record time and memory cost of a process
/usr/bin/time -v [command of process]
```


