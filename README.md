# REGER

In our paper **REGER: Reordering Time Series Data for Regression Encoding in Apache IoTDB**, we show some examples and performance about regression encoding with reordering.

To enable reproductivity, we share all datasets, algorithms and codes in the repository of encoding-reorder, and this readme guides will help you reproduce the results of the experiment and figures in the paper.

## 1. Directory Structure

    ├── README.md           // Help Document
    
    ├── vldb             // Codes and datasets
    
    │   ├── data_draw       // Example data of Figure 9
    
    │   ├── iotdb_datasets_lists      // Datasets of all the experiments
    
    │   ├── figs      // Results of the experiments
    
    │       ├── 0901       // Results of the example
    
    │           ├── result_evaluation         // Example

    |               ├── example100         // Datasets of all the examples
    
    │           └── other .py // // Codes of drawing examples
    
    │   └── other .py       // codes of drawing results

## 2. Environment Requirement

- IoTDB: download from branch [GitHub - apache/iotdb at research/encoding-reorder](https://github.com/apache/iotdb/tree/research/encoding-reorder)
- python: 3.8+
- modules needed: seaborn 0.11.1+, numpy, pandas

## 3. Code Execution

- Get results of compression ratio

```
java  xxx.java
```

- The algorithm corresponding to the java code is as follows

| algorithms                         | java code                                                                        |
| ---------------------------------- |----------------------------------------------------------------------------------|
| Regression Reordering        | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\Reger.java           |
| Varying block size  | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RegerBlockSize.java  |
| Varying blocksize without reordering  | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RegerBlockSizeWithoutReordering.java|
| Varying packsize | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RegerPackSize.java |
| Varying packsize without reordering | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RegerPackSizeWithoutReordering.java |
| Double for regression parameters | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RegerPDouble.java |
| REGER-64-DOUBLE varying block size | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RegerPFloat.java |
| Float for regression parameters   | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\decoder\EncodeTest.java |

- Get figures about xxx.py

```
python xxx.py
```

- The figures corresponding to the python code are as follows

| Figures   | python code                                                                     |
| --------- | ----------------------------------------------------------------------------- |
| Figure 1  | draw_example0_6.py                                                     |
| Figure 2  | draw_example2_5.py                                                            |
| Figure 3  |                                                              |
| Figure 4  | draw_example3.py                                                              |
| Figure 5  | draw_distribution.py                                                          |
| Figure 6  |                                                 |
| Figure 7  | draw_examplea.py                                                          |
| Figure 8  |                                                           |
| Figure 9  | draw_dataall_value_subgraph.py                             |
| Figure 10 | avg_transform_draw.py<br/> draw_compression_ratio.py                          |
| Figure 11 | avg_transform_draw_block_size.py<br/>draw_block_size.py                   |
| Figure 12 | avg_transform_draw_pack_size.py<br/>draw_pack_size.py                   |
| Figure 13 | avg_transform_draw_p.py<br/>draw_p.py                   |


- 
