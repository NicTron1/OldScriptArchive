f12::
toggle := !toggle  ;toggle on off
tooltip % "AutoClicker: " (toggle ? "ACTIVE" : "OFF")
settimer,tooltipoff,1000 ;set a timer for 1 second to clear the tooltip
Click Down
return

tooltipoff:
settimer,tooltipoff,off ;turn the timer off
tooltip ;clear the tooltip
return




