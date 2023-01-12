def addProduct(products, id_barang_new, nama_barang, harga_barang):
    # this function doesn't need return value
    products[id_barang_new]={
        "id_barang": id_barang_new,
        "nama_barang": nama_barang,
        "harga_barang": harga_barang,
    }
     # modify this pass with your own implementation

def calculateTotalPriceAfterDiscount(totalPrice):
    # this function need return value
    if totalPrice >= 500000:
        diskon_penjualan = totalPrice*0.25
    elif totalPrice >= 150000:
        diskon_penjualan = totalPrice*0.10
    else:
        diskon_penjualan= 0 
    totalPrice -= diskon_penjualan
    return totalPrice # modify this return with your own implementation (consider if else threshold for the discount)