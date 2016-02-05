##Directions

Create a probability distribution file is formatted as follows:
.36,.23,.17,.09,.08,.07

If the probability distribution is saved in a file called prob, and the following unix command produces the
optimal encoding scheme:

```cat prob | python multibitsec.py```
The output of this call is:

Total Distortion is 0.550000

[[ 0.36        0          1          2          0.13]

 [ 0.23        1          2          0          0.13]
 
 [ 0.17        2          0          1          0.13]
 
 [ 0.09        3          5          4          0.05]
 
 [ 0.08        4          3          5          0.05]
 
 [ 0.07        5          4          3          0.05]]

 This indicates the inout sources with the corresponding probabilities (column 0) will be encoded by one of three corespnding encodings, indicated by columns 1-3. Column 4 indicates the amount of distortion intoduced by the source symbol. 
