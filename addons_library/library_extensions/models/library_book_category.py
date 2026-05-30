from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _order = "name"

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        (
            "library_book_category_name_unique",
            "unique(name)",
            "Category name must be unique."
        )
    ]