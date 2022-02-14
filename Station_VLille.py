class Station_VLille:
  def __init__(self,record):
    record=record["fields"]
    self.nom=record["nom"]
    self.geo=record["geo"]
    self.vélos=record["nbvelosdispo"]
    self.libres=record["nbplacesdispo"]
    self.état=record["etat"]
    self.color_marker="green"
    if (self.vélos <=2): self.color_marker="orange"
    if (self.libres<=2): self.color_marker="purple"
    if (self.libres<=2 and self.vélos <=2): self.color_marker="purple"
    
    
  def pop(self):
    if self.état=="EN SERVICE":
      état=self.état.lower()
    else:
      état="hs"
      self.color_marker="red"
    return (f"<htlm>{self.nom}<br>{état}<br>vélos: {str(self.vélos)}<br>libres: {str(self.libres)}</html>")