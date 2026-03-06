def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    step = chunk_size-overlap
    ans=[]

    for i in range(0, len(tokens), step):
        chunk = tokens[i : i+chunk_size]
        if chunk:
            ans.append(chunk)
        if i+chunk_size >= len(tokens):
            break

    return ans