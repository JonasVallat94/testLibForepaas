from example.jonas import print_hi
import importlib
foobar = importlib.import_module("example-package-YOUR-USERNAME-HERE")
#import "git+https://github.com/JonasVallat94/testLibForepaas@main"

print_hi("AAA")
foobar.addition(1, 2)