--------------
COMP 4140 Project
Patrick Murphy and Christopher Catton
--------------

--------------
Dependencies
--------------

-numpy
install using PIP: 
    pip install numpy

--------------
Running
--------------

Command Prompt:
runtests

Shell
./runtests

-------------
Directory Structure
-------------

src/
    - contains all the source code
tst/
    - contians all the unit tests and integration test
    - run through the runtests scriot
experiments
    - contains more advanced tests that would have be
    - run through the runexperiments script

-------------
Confusing Filenames
-------------

src/homomorphic_encryption_scheme.py
    - this is the bootstrappable homomorphic encryption scheme
src/somewhat_homomorphic_scheme.py
    - this is the somewhat homomorphic encryption scheme
src/bit_encrypter.py
    - the encryption algorithm
src/evaluate
    - an arbitrary circuit implementation that would be used for the easy specifying of circuits if we had gotten the encryption scheme to work
    