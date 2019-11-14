import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
def test_add_to_cart(browser): 
	browser.get(link)
	time.sleep(30)
	cart = browser.find_elements_by_class_name("btn-add-to-basket")
	assert len(cart) > 0, "Cart not found"
