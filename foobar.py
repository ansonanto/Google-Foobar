'''
    <encrypted>
        CUYZFAgMAQYeUlJTUkYNEw4OEFJBVVUKHQ0GBAoIERBKVUhJVQQZFQ4KCRAJUl5JVQQMBwQdEAZK 
        VUhJVQgEAhkKABwPGRdOXkFNAAgHDRAbEB8MHBVNQVFPQwADGR0KGQQORkdPQwcMFxAABhJNQVFP 
        QwYMExdOXkFNBwQAQ1VXVVUeGw9LRhY= 
    </encrypted>

    For your eyes only! 
'''

import base64

MESSAGE = '''CUYZFAgMAQYeUlJTUkYNEw4OEFJBVVUKHQ0GBAoIERBKVUhJVQQZFQ4KCRAJUl5JVQQMBwQdEAZK 
VUhJVQgEAhkKABwPGRdOXkFNAAgHDRAbEB8MHBVNQVFPQwADGR0KGQQORkdPQwcMFxAABhJNQVFP 
QwYMExdOXkFNBwQAQ1VXVVUeGw9LRhY='''

KEY = 'rajakodumuri'

result = []

for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)
