from treebeard.mp_tree import MP_NodeManager, MP_NodeQuerySet


class CategoryQuerySet(MP_NodeQuerySet):
    def public(self):
        return self.filter(is_public=True)


class CategoryManager(MP_NodeManager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def public(self):
        return self.get_queryset().public()