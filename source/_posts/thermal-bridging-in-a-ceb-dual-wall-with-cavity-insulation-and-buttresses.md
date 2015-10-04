title: " Thermal Bridging in a CEB Dual Wall with Cavity Insulation and Buttresses "
tags:
- Uncategorized
---


Wall systems made of two CEB walls with cavity insulation lead to unusual (to other wall systems) thermal bridging problems.

Say you have two walls made of 4" wide block forming a 12" insulation cavity. CEBs have r-value of 0.25 while insulation have an r-value of 2.7. The total r-value is roughly 34.4 which is great:

```
0.25*4" + 2.7*12" + 0.25*4" => 34.4
```
Suppose that every 4 blocks, you place a block lengthwise to add some micro-buttresses which give extra strength to the wall. According to the typical linear r-value method, you would do a weighted average of the two different situations:

```
12" of insulation: 0.25*4" + 2.7*12" + 0.25*4" => 34.4
4" of insulation: 0.25*12" + 2.7*4" + 0.25*4" => 14.8
weighted average (24" of 12" thick insulation for every 4" of 4" thick insulation):
    (34.4*24" + 14.8*4")/28" => 31.6
```
This predicts only a small 8.1% decrease in average r-value resulting in 8.8% of additional heat loss. Not bad given the huge amount of extra strength the micro-buttresses add.

![/images/wall.png](/images/wall.png)

## Therm
I've modeled this wall system in THERM, and due to the conductivity of the CEB blocks the heat loss is actually much worse. A rough reading of the renderings THERM provides predicts roughly 50% more heat loss with the buttresses than without. This is because heat travels so well through the CEBs. In areas near to the 4" insulation gap, heat will collect over a large area of the CEB wall, funnel into the 4" thermal bridge and then spread out along the outside wall.

In the diagrams below, you can see the top half of the wall which has no buttresses, and the wall section below which does. The color indicates heat flow in BTU/hr*ft^2. High numbers are bad. I've set up the scale of the left diagram so that any white section indicates that the heat loss is more than 20% higher than it would be without the buttresses. This is most of the wall. In the second diagram you can see that large sections of the wall are loosing heat at 2.5x the rate that they would without the buttresses.

![/images/wall-20p.png](/images/wall-20p.png) ![/images/wall250p.png](/images/wall250p.png)

## Conclusion
Adding buttresses can help with the strength of the wall, but detrimentally effect the insulating value of your cavity.

## The Flip Side
On the other hand, CEBs high conductivity makes them great at quickly absorbing and evenly distributing heat throughout the house that is gained through passive solar design. They act as great heat sinks in the winter and cool sinks in the summer.

[Here](/files/CEB-Bridge-ose.THM) is the THERM model used in the above examples

Note to OSE Microhouse designers: I haven't run this example with your proposed 2" thermal breaks, but I imagine that they will loose heat at least twice as fast as a linear analysis might predict.


