

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

# f Float and .Nf N= the number of decimal places
# ex: {:.2f} will round the float to 2 decimal places
pi = 3.141592653589793238462643383279502884197169
print('Pi is approximately {:.2f}'.format(pi));
print('{0:<8} | {1:^8}| {2:>8.2f}'.format(first, second, pi));
