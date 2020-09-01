import timeit
import functools
from src.common import lookandsay as common_lookandsay
from src.cosmo import lookandsay as cosmo_lookandsay

SEQUENCE_INDEX = 50

t = timeit.Timer(functools.partial(common_lookandsay.get_sequence, SEQUENCE_INDEX))
print(f"Common solution: {t.timeit(50)}")

t = timeit.Timer(functools.partial(cosmo_lookandsay.get_sequence, SEQUENCE_INDEX))
print(f"Cosmo solution: {t.timeit(50)}")
