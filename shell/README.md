## Collection of basic commands
```bash
# compression
tar -zcvf example.tar.gz PATH/
# unzip
tar -zxvf example.tar.gz
tar -jxvf example.tar.bz2

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
```
