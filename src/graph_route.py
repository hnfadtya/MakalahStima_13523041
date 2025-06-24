graph_route = {'Cikarang': {
    'coords': (10, 6), 
    'edges': [('Bekasi', 21, 'KRL')]}, 
'Bekasi': {
    'coords': (9, 6), 
    'edges': [('Jatinegara', 19, 'KRL')]}, 
'Jatinegara': {
    'coords': (8, 6), 
    'edges': [('Matraman', 2, 'KRL'), ('Senen Sentral', 13, 'KRL'), ('Bekasi', 19, 'KRL')]}, 
'Matraman': {
    'coords': (7, 6), 
    'edges': [('Jatinegara', 2, 'KRL'), ('Manggarai', 2, 'KRL'), ('Senen Sentral', 32, 'TJ'), ('LRT Cawang', 30, 'TJ')]}, 
'Manggarai': {
    'coords': (5, 6), 
    'edges': [('Matraman', 2, 'KRL'), ('Sudirman / Dukuh Atas', 13, 'KRL'), ('Jakarta Kota', 20, 'KRL'), ('Cikoko', 5, 'KRL')]}, 
'Sudirman / Dukuh Atas': {
    'coords': (5, 5), 
    'edges': [('Manggarai', 13, 'KRL'), ('Pancoran', 13, 'LRT'), ('Bendungan Hilir / Semanggi', 11, 'TJ'), ('Tanah Abang', 5, 'KRL'), ('Bundaran HI', 8, 'TJ'), ('Bendungan Hilir / Semanggi', 4, 'MRT'), ('Bundaran HI', 3, 'MRT')]}, 
'Tanah Abang': {
    'coords': (4, 5), 
    'edges': [('Sudirman / Dukuh Atas', 5, 'KRL'), ('Kebayoran', 11, 'KRL'), ('Duri', 8, 'KRL')]}, 
'Duri': {
    'coords': (3, 5), 
    'edges': [('Tanah Abang', 8, 'KRL'), ('Grogol', 4, 'KRL')]}, 
'Tangerang': {
    'coords': (1, 5), 
    'edges': [('Taman Kota', 20, 'KRL')]}, 
'Taman Kota': {
    'coords': (2, 5), 
    'edges': [('Tangerang', 20, 'KRL'), ('Grogol', 5, 'KRL')]}, 
'Grogol': {
    'coords': (3, 6), 
    'edges': [('Taman Kota', 5, 'KRL'), ('Duri', 4, 'KRL'), ('Bendungan Hilir / Semanggi', 38, 'TJ')]}, 
'Serpong': {
    'coords': (1, 2), 
    'edges': [('Pondok Ranji', 14, 'KRL')]}, 
'Pondok Ranji': {
    'coords': (2, 3), 
    'edges': [('Serpong', 14, 'KRL'), ('Kebayoran', 7, 'KRL')]}, 
'Kebayoran': {
    'coords': (3, 4), 
    'edges': [('Pondok Ranji', 7, 'KRL'), ('Tanah Abang', 11, 'KRL'), ('Blok M / ASEAN', 18, 'TJ')]}, 
'Bogor': {
    'coords': (2, -1), 
    'edges': [('Citayam', 20, 'KRL')]}, 
'Citayam': {
    'coords': (3, 0), 
    'edges': [('Bogor', 20, 'KRL'), ('Depok', 10, 'KRL')]}, 
'Depok': {
    'coords': (4, 1), 
    'edges': [('Citayam', 10, 'KRL'), ('Cikoko', 23, 'KRL')]}, 
'Cikoko': {
    'coords': (5, 2), 
    'edges': [('Depok', 23, 'KRL'), ('Manggarai', 5, 'KRL'), ('Pancoran', 4, 'LRT'), ('Pancoran', 5, 'TJ'), ('LRT Cawang', 3, 'LRT'), ('LRT Cawang', 4, 'TJ')]}, 
'Bekasi Barat': {
    'coords': (9, 5), 
    'edges': [('LRT Cawang', 28, 'LRT')]}, 
'LRT Cawang': {
    'coords': (6, 2), 
    'edges': [('Bekasi Barat', 28, 'LRT'), ('Cikoko', 3, 'LRT'), ('Cikoko', 4, 'TJ'), ('Matraman', 30, 'TJ')]}, 
'Pancoran': {
    'coords': (5, 3), 
    'edges': [('Sudirman / Dukuh Atas', 13, 'LRT'), ('Cikoko', 4, 'LRT'), ('Cikoko', 5, 'TJ'), ('Bendungan Hilir / Semanggi', 12, 'TJ'), ('Blok M / ASEAN', 15, 'TJ')]}, 
'Lebak Bulus': {
    'coords': (3, 2), 
    'edges': [('Blok M / ASEAN', 20, 'MRT')]}, 
'Blok M / ASEAN': {
    'coords': (4, 4), 
    'edges': [('Lebak Bulus', 20, 'MRT'), ('Bendungan Hilir / Semanggi', 6, 'MRT'), ('Bendungan Hilir / Semanggi', 30, 'TJ'), ('Pancoran', 15, 'TJ'), ('Kebayoran', 18, 'TJ')]}, 
'Bendungan Hilir / Semanggi': {
    'coords': (5, 4), 
    'edges': [('Blok M / ASEAN', 6, 'MRT'), ('Sudirman / Dukuh Atas', 4, 'MRT'), ('Blok M / ASEAN', 30, 'TJ'), ('Sudirman / Dukuh Atas', 11, 'TJ'), ('Pancoran', 12, 'TJ'), ('Grogol', 38, 'TJ')]}, 
'Bundaran HI': {
    'coords': (6, 5), 
    'edges': [('Sudirman / Dukuh Atas', 3, 'MRT'), ('Sudirman / Dukuh Atas', 8, 'TJ'), ('Monas', 10, 'TJ')]}, 
'Monas': {
    'coords': (6, 6), 
    'edges': [('Jakarta Kota', 28, 'TJ'), ('Juanda', 9, 'TJ'), ('Bundaran HI', 10, 'TJ')]}, 
'Jakarta Kota': {
    'coords': (7, 9), 
    'edges': [('Monas', 28, 'TJ'), ('Manggarai', 20, 'KRL')]}, 
'Juanda': {
    'coords': (7, 8), 
    'edges': [('Senen Sentral', 25, 'TJ'), ('Monas', 9, 'TJ')]}, 
'Senen Sentral': {
    'coords': (7, 7), 
    'edges': [('Jatinegara', 13, 'KRL'), ('Juanda', 25, 'TJ'), ('Matraman', 32, 'TJ')]}}