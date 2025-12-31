python script to try to make a funny pattern in wordle 

usage:
```
uv run main.py [-h] [-d {error,debug,info}] answer

wordle 67 solver

positional arguments:
  answer                wordle answer

options:
  -h, --help            show this help message and exit
  -d, --debug {error,debug,info}
                        set log level
```



todo:
1. cant have multiple letters for yellow unless the word has those letters
    e.g. `batch` has 1 t, cant use `blatt` for 2nd row - would just be `X*__*` not `X*___`
2. find some api to get the daily wordle answer instead of cli arg
3. process word once into a file and load that file instead of processing every time
4. the word list that is being used is probably not correct anymore
5. add an arg for leniency (probably a bunch of work tbh)

too lazy to implement now
<div style="display:flex">
<img width="128" height="128" alt="glorp" src="https://github.com/user-attachments/assets/113e38ae-8c8c-4ffa-85ff-2cd7399c1c79" />
<img width="128" height="128" alt="cateat" src="https://github.com/user-attachments/assets/c2ede6bf-0fda-4c49-bbf8-426e65586045" />
</div>

