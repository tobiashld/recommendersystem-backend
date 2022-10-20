from src.service.recommenderservice import get_neighbors,get_shared_neighbors_for_list

def test_get_neighbors():
    """ 
    Es wird die Verbindung der Matrix getestet und die Fähigkeit 
    Nachbarn aus der Matrix auszulesen
    """
    assert get_neighbors(1) == [1,694,5302,4181,1084,13586,10257,1173,8800,15100,10495]

def test_get_shared_neighbors_for_list():
    """
    Es wird die Verbindung der Matrix getestet und die Fähigkeit 
    mehrere Nachbarn in eine fixe Liste zu packen
    """
    assert get_shared_neighbors_for_list([1,2,3]) == [694, 5302, 4181, 15376, 11212, 7195, 7293, 4628, 3301]
