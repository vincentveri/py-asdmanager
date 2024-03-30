from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from . import db

from datetime import date

class Utente(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()


class Cliente(db.Model):
    __tablename__ = "cliente"

    id: Mapped[int] = mapped_column(primary_key=True)
    documenti: Mapped[List["Documento"]] = relationship()
    nome: Mapped[str]
    cognome: Mapped[str]
    codice_fiscale: Mapped[str]


class Documento(db.Model):
    __tablename__ = "documento"

    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[int]
    numeratore: Mapped[str]
    data_emissione: Mapped[date]
    codice_fiscale: Mapped[str]
    descrizione: Mapped[str]
    cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id"))
    cliente: Mapped["Cliente"] = relationship(back_populates="documenti")