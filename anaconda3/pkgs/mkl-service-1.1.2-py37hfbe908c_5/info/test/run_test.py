#  tests for mkl-service-1.1.2-py37hfbe908c_5 (this is a generated file);
print('===== testing package: mkl-service-1.1.2-py37hfbe908c_5 =====');
print('running run_test.py');
#  --- run_test.py (begin) ---
import mkl
import mkl.test

for s in ('mkl.get_max_threads()', 'mkl.get_cpu_clocks()', 'mkl.mem_stat()',
          'mkl.get_cpu_frequency()', 'mkl.get_version_string()'):
    print('%s=%r' % (s, eval(s)))

assert mkl.test.run().wasSuccessful()
assert 'Math Kernel Library Version 20' in mkl.get_version_string()
print(mkl.__version__)
assert mkl.__version__ == '1.1.2'
#  --- run_test.py (end) ---

print('===== mkl-service-1.1.2-py37hfbe908c_5 OK =====');
print("import: 'mkl'")
import mkl

print("import: 'mkl.service'")
import mkl.service

