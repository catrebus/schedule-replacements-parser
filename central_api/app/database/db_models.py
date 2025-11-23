from typing import Optional
import datetime

from sqlalchemy import Date, DateTime, ForeignKeyConstraint, Index, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from central_api.app.database import Base


class CollegeGroup(Base):
    __tablename__ = 'college_group'
    __table_args__ = (
        Index('id_UNIQUE', 'id', unique=True),
    )

    id: Mapped[str] = mapped_column(String(10), primary_key=True)

    replacement: Mapped[list['Replacement']] = relationship('Replacement', back_populates='college_group')


class PdfDownloadUrl(Base):
    __tablename__ = 'pdf_download_url'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)

    replacement: Mapped[list['Replacement']] = relationship('Replacement', back_populates='url')


class Type(Base):
    __tablename__ = 'type'

    type: Mapped[str] = mapped_column(String(45), primary_key=True)

    replacement_type: Mapped[list['ReplacementType']] = relationship('ReplacementType', back_populates='type_')


class Replacement(Base):
    __tablename__ = 'replacement'
    __table_args__ = (
        ForeignKeyConstraint(['group'], ['college_group.id'], name='group_id_replacement'),
        ForeignKeyConstraint(['url_id'], ['pdf_download_url.id'], name='url_id_replacement'),
        Index('group_id_replacement_idx', 'group'),
        Index('url_id_replacement_idx', 'url_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    group: Mapped[str] = mapped_column(String(10), nullable=False)
    url_id: Mapped[int] = mapped_column(Integer, nullable=False)
    teacher_before: Mapped[Optional[str]] = mapped_column(String(45))
    pair_number_before: Mapped[Optional[int]] = mapped_column(Integer)
    discipline_before: Mapped[Optional[str]] = mapped_column(String(255))
    class_before: Mapped[Optional[str]] = mapped_column(String(45))
    teacher_now: Mapped[Optional[str]] = mapped_column(String(45))
    pair_number_now: Mapped[Optional[int]] = mapped_column(Integer)
    discipline_now: Mapped[Optional[str]] = mapped_column(String(255))
    class_now: Mapped[Optional[str]] = mapped_column(String(45))

    college_group: Mapped['CollegeGroup'] = relationship('CollegeGroup', back_populates='replacement')
    url: Mapped['PdfDownloadUrl'] = relationship('PdfDownloadUrl', back_populates='replacement')
    replacement_type: Mapped[list['ReplacementType']] = relationship('ReplacementType', back_populates='replacement')


class ReplacementType(Base):
    __tablename__ = 'replacement_type'
    __table_args__ = (
        ForeignKeyConstraint(['replacement_id'], ['replacement.id'], name='replacement_id_replacement_type'),
        ForeignKeyConstraint(['type'], ['type.type'], name='type_id_replacement_type'),
        Index('replacement_id_replacement_type_idx', 'replacement_id'),
        Index('type_id_replacement_type_idx', 'type')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    replacement_id: Mapped[int] = mapped_column(Integer, nullable=False)
    type: Mapped[str] = mapped_column(String(45), nullable=False)

    replacement: Mapped['Replacement'] = relationship('Replacement', back_populates='replacement_type')
    type_: Mapped['Type'] = relationship('Type', back_populates='replacement_type')