# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    p_hash = 0
    t_hash = 0
    prime = 101
    base = 256
    result = []

    # Calculate hash of pattern and the first window of text
    for i in range(p_len):
        p_hash = (p_hash * base + ord(pattern[i])) % prime
        t_hash = (t_hash * base + ord(text[i])) % prime

    # Slide the pattern over text one by one
    for i in range(t_len - p_len + 1):
        # Check if hash values of the current window of text and pattern are the same
        if p_hash == t_hash:
            # Check the characters one by one to confirm the match
            if text[i:i + p_len] == pattern:
                result.append(i)
        
        # Calculate hash for the next window of text
        if i < t_len - p_len:
            t_hash = (t_hash * base - ord(text[i]) * pow(base, p_len, prime) + ord(text[i + p_len])) % prime
            # We might get negative values of t_hash, converting it to positive
            if t_hash < 0:
                t_hash += prime

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

