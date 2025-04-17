import rasterio

with rasterio.open('/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Large-files/RGB-UTM32/DTM-source-9mm.tif') as src:
    dtm_crs = src.crs
    print("DTM CRS:", dtm_crs)
