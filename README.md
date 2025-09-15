# workshop

1) pwd and ls 

2) grep PING hints.txt -c

3) sort -u order.txt

4) cut -c 1 stack.txt 

5) tr '[:upper:]' '[:lower:]' < motto.txt

6) tail -n 1 alpha/clue.txt

7) head -n 3 logs.txt; tail -n 2 logs.txt

8) -rw--w--w- 1 codespace codespace 26 Sep 15 10:01 secret.txt

9) { cut -d' ' -f6 alpha/clue.txt | tr -d '"'; sed -n '2p' alpha/clue.txt | cut -d' ' -f5; cut -d' ' -f5 charlie/secret.txt; } | tr '\n' ' '
