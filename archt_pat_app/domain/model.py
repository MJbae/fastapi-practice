# from __future__ import annotations
# from dataclasses import dataclass
# from datetime import date
# from typing import Optional, List, Set
#
#
# class Product:
#     def __init__(self, sku: str, batches: List[Batch], version_number: int = 0):
#
#
# @dataclass(unsafe_hash=True)
# class OrderLine:
#
#
# class Batch:
#     def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
#
#     def __repr__(self):
#
#     def __eq__(self, other):
#
#     def __hash__(self):
#
#     def __gt__(self, other):
#
#     def allocate(self, line: OrderLine):
#
#     def deallocate_one(self) -> OrderLine:
#
#     @property
#     def allocated_quantity(self) -> int:
#
#     @property
#     def available_quantity(self) -> int:
#
#     def can_allocate(self, line: OrderLine) -> bool:
