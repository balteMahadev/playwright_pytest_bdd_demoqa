from pages.login import LoginPage
from pages.products import ProductsPage

# from pages.dashboard_page import DashboardPage as dashboard
# from pages.profile_page import ProfilePage as profile

PAGE_OBJECTS = {
    "login": LoginPage,
    "products": ProductsPage,
    # "profile": profile,
}


class PageFactory:
    @staticmethod
    def get_page(page, page_name: str):
        """
        Return the page object instance (like LoginPage, ProductsPage, etc.)
        """
        page_name = page_name.lower()
        if page_name not in PAGE_OBJECTS:
            raise ValueError(f"[ERROR] Page '{page_name}' not found.")

        page_obj_class = PAGE_OBJECTS[page_name]
        return page_obj_class(page)

    @staticmethod
    def get_element(page, page_name: str, element_name: str):
        """
        Return the specific element from the page object.
        """
        page_obj = PageFactory.get_page(page, page_name)

        # Directly access the element name without converting to snake_case
        if not hasattr(page_obj, element_name):
            raise AttributeError(f"[ERROR] Element '{element_name}' not found in {page_name} page.")

        return getattr(page_obj, element_name)
