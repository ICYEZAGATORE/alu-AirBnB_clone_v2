from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """State model to store state information."""
    
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """Getter for FileStorage to return a list of City instances."""
        if models.storage_t == 'db':
            return self.cities
        else:
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
