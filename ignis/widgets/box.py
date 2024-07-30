from gi.repository import Gtk, GObject
from ignis.base_widget import BaseWidget
from typing import List


class Box(Gtk.Box, BaseWidget):
    """
    Bases: `Gtk.Box <https://lazka.github.io/pgi-docs/#Gtk-4.0/classes/Box.html>`_.

    The main layout widget.

    .. hint::
        You can use generators to set children.

        .. code-block::

            Widget.Box(
                child=[Widget.Label(label=str(i)) for i in range(10)]
            )

    Properties:
        - **child** (``List[Gtk.Widget]``, optional, read-write): The list of child widgets.
        - **vertical** (``bool``, optional, read-write): Whether the box arranges children vertically.

    .. code-block:: python

        Widget.Box(
            child=[Widget.Label(label='heh'), Widget.Label(label='heh2')],
            vertical=False,
            homogeneous=False,
            spacing=52
        )
    """

    __gtype_name__ = "IgnisBox"
    __gproperties__ = {**BaseWidget.gproperties}

    def __init__(self, **kwargs):
        Gtk.Box.__init__(self)
        self._child = []
        BaseWidget.__init__(self, **kwargs)

    @GObject.Property
    def child(self) -> List[Gtk.Widget]:
        return self._child

    @child.setter
    def child(self, child: List[Gtk.Widget]) -> None:
        for c in self._child:
            self.remove(c)
        self._child = []
        for c in child:
            if c:
                self.append(c)
                self._child.append(c)

    def append(self, child: Gtk.Widget) -> None:
        self._child.append(child)
        super().append(child)

    def remove(self, child: Gtk.Widget) -> None:
        self._child.remove(child)
        super().remove(child)

    def prepend(self, child: Gtk.Widget) -> None:
        self._child.insert(0, child)
        super().prepend(child)

    @GObject.Property
    def vertical(self) -> bool:
        return self.get_orientation() == Gtk.Orientation.VERTICAL

    @vertical.setter
    def vertical(self, value: bool) -> None:
        if value:
            self.set_property("orientation", Gtk.Orientation.VERTICAL)
        else:
            self.set_property("orientation", Gtk.Orientation.HORIZONTAL)
