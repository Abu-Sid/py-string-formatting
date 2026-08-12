

# string formatting
first = 'I';
second= 'love';
third = 'apple';

version = 3;
print('i love python ')
print('{} {} {}'.format(first, second, third));
print('i love python {}'.format(version));

# "<" left(default) "^"center and ">" right alignment

print('{0:<8} | {1:^8}| {2:>8}'.format(first, second, third));