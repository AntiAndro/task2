import sys

from geocoder import get_ll_span
from mapapi_PG import show_map

toponym_to_find = " ".join(sys.argv[1:])
if toponym_to_find:
    ll, spn = get_ll_span(toponym_to_find)
    show_map(ll_spn=f'll={ll}&spn={spn}', map_type="map", add_params=f'pt={ll}')
else:
    print('No toponym')