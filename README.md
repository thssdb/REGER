# REGER

In our paper **REGER: Reordering Time Series Data for Regression Encoding in Apache IoTDB**, we show some examples and performance about regression encoding with reordering.

To enable reproductivity, we share all datasets, algorithms and codes in the repository of encoding-reorder, and this readme guides will help you reproduce the results of the experiment and figures in the paper.

## 1. Directory Structure

    ├── README.md           // Help Document
    
    ├── compression_ratio  // Results
    
    │    ├── p_float_vary_p   // Result
    
    │    ├── pack_size_float   // Result
    
    │    ├── regulr_float   // Result
    
    │    ├── sota_ratio   // Result
    
    ├── data_draw  // Data for drawing some figures
    
    ├── example  // Results
    
    │    ├── result_evaluation   // Example

    |         ├── example100     // Datasets of examples
    
    │    └── other .py // // Codes of drawing examples
    
    ├── figs  // Figures
    
    ├── iotdb_datasets_lists      // Datasets of all the experiments
    
    └── other .py       // codes of drawing results

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
| Regression Reordering        | iotdb\iotdb-core\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\REGERFloatTest.java           |
| Varying p  | iotdb\iotdb-core\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\REGERPFloatTest.java  |

- Get figures about xxx.py

```
python xxx.py
```

- The figures corresponding to the python code are as follows

| Figures   | python code                                                                     |
| --------- | ----------------------------------------------------------------------------- |
| Figure 1  | draw_example0_63.py                                                     |
| Figure 2  | draw_example2_5.py                                                            |
| Figure 3  |                                                              |
| Figure 4  | draw_example3_2.py                                                              |
| Figure 5  | draw_distribution.py                                                          |
| Figure 6  |                                                 |
| Figure 7  | draw_examplea2.py                                                          |
| Figure 8  |                                                           |
| Figure 9  | draw_dataall_value_subgraph.py                             |
| Figure 10 | avg_transform_draw.py<br/>draw_compression_ratio.py                          |
| Figure 11 | avg_transform_draw.py<br/>draw_compression_ratio.py                   |
| Figure 12 | avg_transform_draw.py<br/>draw_compression_ratio.py                   |
| Figure 13 | avg_float_block_size.py<br/>draw_block_size_float.py                |
| Figure 14 | avg_float_pack_size.py<br/>draw_pack_size_float.py     
| Figure 15 | avg_transform_draw_p.py<br/>draw_p.py       

