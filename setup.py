from distutils.core import setup, Extension
 
 
example_module = Extension('_example',
                           sources=['example_wrap.cxx', 'example.cpp'],
                           )
 

setup (name = 'example',
       version = '0.1',
       author      = "keke",
       description = """CPP Says Hello  to Python""",
       ext_modules = [example_module],
       py_modules = ["example"],
       )