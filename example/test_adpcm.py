from codec import encode_block,decode_block

with open('sft8k.pcm','rb') as f,open('sft8k-out.pcm','wb') as f2:
    chunk_size = 1010
    while True:
        chunk =f.read(chunk_size)
        if not chunk:
            break
        tmp = encode_block(chunk)
        f2.write(decode_block(tmp))

with open('sft16k.pcm','rb') as f,open('sft16k-out.pcm','wb') as f2,open('sft16k.ima','wb') as f3:
    chunk_size = 1010
    while True:
        chunk =f.read(chunk_size)
        if not chunk:
            break
        tmp = encode_block(chunk)
        f3.write(tmp)
        f2.write(decode_block(tmp))

