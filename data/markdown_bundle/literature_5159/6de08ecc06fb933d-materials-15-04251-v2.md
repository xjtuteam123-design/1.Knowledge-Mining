# materials-15-04251-v2

<!-- source: D:\总文献\materials-15-04251-v2.pdf -->
<!-- file_sha256: 26b1b0fde11d218a3cc5099cd7de5c0f624e6d72629d5e2cbcd49ed1fd5b0516 -->

## Page 1

/gid00030/gid00035/gid00032/gid00030/gid00038/gid00001/gid00033/gid00042/gid00045/gid00001
/gid00048/gid00043/gid00031/gid00028/gid00047/gid00032/gid00046
Citation: Li, W.; Li, W.; Qin, Z.; Tan,
L.; Huang, L.; Liu, F.; Xiao, C. Deep
Transfer Learning for Ni-Based
Superalloys Microstructure
Recognition on γ′ Phase. Materials
2022, 15, 4251. https://doi.org/
10.3390/ma15124251
Academic Editor: Yurii Sharkeev
Received: 29 April 2022
Accepted: 13 June 2022
Published: 15 June 2022
Publisher’s Note:MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional afﬁl-
iations.
Copyright: © 2022 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
materials
Article
Deep Transfer Learning for Ni-Based Superalloys
Microstructure Recognition on γ′ Phase
Wenyi Li 1, Weifu Li 1,2
 , Zijun Qin 3, Liming Tan 3, Lan Huang 3, Feng Liu 3
 and Chi Xiao 4,*
1 College of Science, Huazhong Agricultural University, Wuhan 430070, China;
wenyili@webmail.hzau.edu.cn (W.L.); liweifu@mail.hzau.edu.cn (W.L.)
2 Hubei Key Laboratory of Applied Mathematics, Hubei University, Wuhan 430062, China
3 State Key Laboratory of Powder Metallurgy, Central South University, Changsha 410083, China;
zijun.qin@csu.edu.cn (Z.Q.); limingtan@csu.edu.cn (L.T.); lhuang@csu.edu.cn (L.H.); liufeng@csu.edu.cn (F.L.)
4 Key Laboratory of Biomedical Engineering of Hainan Province, School of Biomedical Engineering,
Hainan University, Haikou 570228, China
* Correspondence: xiaochi@hainanu.edu.cn
Abstract: Ni-based superalloys are widely used to manufacture the critical hot-end components
of aviation jet engines and various industrial gas turbines. The analysis of Ni-based superalloys
microstructures is an important research task during the design and development of superalloys. The
material microstructure information can only be understood by experts in the long history. Image
segmentation and recognition are developing techniques for accelerating the microstructure analysis
automatically. Although deep learning techniques have achieved satisfactory performance, they
usually suffer from generalization, i.e., performing worse on a new dataset. In this paper, a deep
transfer learning method which just needs a small number of labeled images is proposed to perform
the microstructure recognition on γ′ phase. To evaluate the effectiveness, we homely prepare two
Ni-based superalloys at temperatures 900 ◦C and 1000 ◦C, and manually annotate two datasets
named as W-900 and W-1000. Experimental results demonstrate that the proposed method only
needs 3 and 5 labeled images to achieve state-of-the-art segmentation accuracy during the transfer
from W-900 to W-1000 and the transfer from W-1000 to W-900, while enjoying the advantage of fast
convergence. In addition, a simple and effective software for the Ni-based superalloys microstructure
recognition on γ′ phase is developed to improve the efﬁciency of materials experts, which will greatly
facilitate the design of new Ni-base superalloys and even other multicomponent alloys.
Keywords: superalloys; scanning electron microscop; deep transfer learning; microstructure charac-
terization; software; accelerating design
1. Introduction
Ni-based superalloys [1,2] have been widely used in aerospace, marine, energy and
other ﬁelds because of its high temperature strength, good oxidation resistance, corrosion
resistance, fatigue resistance and other comprehensive properties, which are fundamentally
controlled by the internal microstructure and compositions [3–5]. Ni-based superalloys
usually contain more than eight metal elements. The modiﬁcation on any alloy composition
may cause a signiﬁcant change of the precipitated phase and mechanical properties [ 6].
The phases of Ni-based superalloys generally include γ, γ′, TCP and GCP phases, where
γ′ is the major phase yielding precipitation strengthening and its volume fraction and
particle size play dominating roles in alloy performance [7,8]. Therefore, it is essential to
obtain the accurate and reliable data on γ′ phase distribution, which can be achieved using
microstructure recognition technology [9,10].
Typically, the evaluation and analysis of the microstructure are conducted by experi-
enced experts with knowledge of materials and microstructural characterization [11–13].
This artiﬁcial process requires speciﬁc training and it is sluggish. With the development
of computer science, microstructure can be recognized automatically. To be speciﬁc, the
Materials 2022, 15, 4251. https://doi.org/10.3390/ma15124251 https://www.mdpi.com/journal/materials

## Page 2

Materials 2022, 15, 4251 2 of 10
microstructure recognition [14] involves the image acquisition, processing, segmentation,
information extraction, statistical analysis, and visualization. The subject of microstructure
segmentation consists of a set of problems that are central to the disciplines of microstruc-
ture recognition.
Currently, a commonly used method for microstructure recognition of Ni-based super-
alloys is based on threshold [15]. However, it is difﬁcult to ﬁnd a ﬁxed threshold to process
different images or different regions in one image, especially when the image background
or the feature intensities are heterogeneous. To this end, an adaptive method was developed
and implemented to automatically adjust the threshold value for local pixel intensity [16].
Although the adaptive threshold seems to be a robust method to circumvent the above
limitations, it also requires other advanced ﬁltering methods and to be adjusted manually
by materials experts. Recently, Kondo et al. [17] demonstrated that deep learning is useful
for microstructure recognition to reveal the microstructure-property linkage in materials.
Jia et al. [18] proposed an end-to-end network architecture that could accurately identify
the γ′ phase in Ni-based superalloys. Although achieving satisfactory performance, these
methods usually suffer from generalization when the data distribution changes. It means
that existing methods will perform worse on a new Ni-based superalloys dataset produced
at different conditions. In fact, they require a large number of pixel-level labeled images to
train a new model, which is labor-intensive and time-consuming.
To address this problem, we propose to adopt deep transfer learning for microstructure
recognition on γ′ phase due to its success in computer vision [19,20]. The objective is to
settle how to use a small number of labeled images to achieve outstanding γ′ phase
recognition for a new Ni-based superalloys dataset. The main contributions of this paper
can be roughly grouped in three different directions summarized as follows:
1. Method: We propose a deep transfer learning method for identifying the γ′ phase on
Ni-based superalloys datasets. It can take full use of existing labeled images and train
the deep learning model with a few labeled images. To the best of our knowledge, it
may be the ﬁrst endeavor on this topic;
2. Dataset: To evaluate the effectiveness of the proposed method, two Ni-based superal-
loys are prepared at temperatures 900◦C and 1000◦C, and two datasets are annotated
manually after acquisition and processing;
3. Application: We develop a simple and effective software for the Ni-based superalloys
microstructure recognition on γ′ phase, to help the materials experts. The code has
been provided publicly (github.com/258yujin/transfer_learning_software, accessed
on 23 April 2022) and can also be applied to other multicomponent alloys.
The rest of this paper is organized as follows. Section 2 introduces the high throughput
experimental preparation process of Ni-based superalloys. Section 3 states the details of
the proposed deep transfer learning method. Section 4 reports the experimental analysis of
our approach. Section 5 presents the details of the developed software. Finally, Section 6
closes this paper with conclusion.
2. Materials
A high throughput method was applied to obtain adequate microstructural informa-
tion. As a typical high throughput sample with gradient composition, multicomponent dif-
fusion multiple (MCDM) was designed and employed to obtain a composition-dependent
microstructure [21]. Taking W1-W3-W4 (designed as NiX-6W-6Mo) diffusion triple as an
example to illustrate the steps for MCDM preparation and characterization, as shown in
Figure 1a, the MCDM was obtained through assembling alloys with different composi-
tions, as listed in Table 1, followed by electron-beam welding, hot isostatic pressing, and
heat treatment. Thereafter, wide composition gradients and diverse microstructures were
generated in a single sample. To observe the precipitates, the sample was etched in the
solution of 33% H2O + 33% acetic acid + 33% HNO3 + 1%HF for 5–10 s, and characterized
via Zeiss Supra 55 ﬁeld emission scanning electron microscope (SEM) equipped with an
ATLAS large-area imaging software, which could automatically capture and join images.

## Page 3

Materials 2022, 15, 4251 3 of 10
To be speciﬁc, the SEM images with a pixel resolution of 20 nm were obtained by using
back-scattered electron (BSE) and secondary electron (SE) modes simultaneously. As shown
in Figure 1b, there is a big difference between the microstructures at temperatures 900◦C
and 1000◦C. Thus, the integrated images with different precipitate characteristics were
obtained for further microstructure recognition.
(a)
(b)
Figure 1. (a) The high throughput experimental preparation process of Ni-based superalloys; (b) The
acquired microstructure by SEM at temperatures 900◦C and 1000◦C.
Table 1. Measured composition of simple W1–W7 in wt.%.
Co W Mo Cr Al Ti Ta Nb Hf Ni
W1 13.0 3.0 2.9 12.2 3.03 3.96 3.1 - 0.21 Bal.
W2 27.8 3.0 2.9 12.0 3.05 4.06 3.0 - 0.21 Bal.
W3 13.0 6.1 2.9 11.8 3.05 3.92 3.0 - 0.22 Bal.
W4 13.1 3.0 6.0 12.1 3.05 4.08 3.1 - 0.19 Bal.
W5 13.0 2.9 3.0 12.0 3.07 6.01 3.0 - 0.19 Bal.
W6 13.0 3.0 2.9 12.0 3.10 4.04 8.1 - 0.20 Bal.
W7 13.0 3.0 3.0 11.9 2.98 4.12 3.0 4.0 0.22 Bal.
3. Methods
In this section, the deep transfer learning method for identifying the γ′ phase on
Ni-based superalloys datasets is introduced. To better evaluate and illustrate the method,
we have manually annotated the pixel-levelγ′ phase from the SEM images of two Ni-based
superalloys produced at temperatures 900 ◦C and 1000 ◦C, which are named as W-900
(including 148 images with size 512× 512) and W-1000 (including 100 images with size
512× 512), respectively. Given the whole labeled images in the W-900 and a few labeled
images in the W-1000, the schematic ﬂowchart of the proposed transfer method from W-900
(referred as source domain) to W-1000 (referred as target domain) is presented in Figure 2.
The training process of deep transfer learning is roughly summarized as follows. First,
we train the basic network fully with the whole 148 images in the W-900. During the
training, the Adam algorithm is adopted with a learning rate of 0.0001 to optimize the
model. The batch size is set as 2 and the epoch is set as 50. Meanwhile, the data aug-
mentation, including ﬂipping, rotation and adding Gaussian noise is adopted to improve

## Page 4

Materials 2022, 15, 4251 4 of 10
the generalization performance. It is well known that the shallow layers of deep neural
network extract low-level general features that are suitable for common tasks, while the
deep layers extract more advanced features that are highly dependent on speciﬁc data and
mission [22]. Inspired by Ref. [ 22], we similarly freeze the weights in the encoder layers
and ﬁne-tune the weights in the decoder layers by a small number of images in the W-1000.
During the ﬁne-tuning, we adopt the common strategy of halving the initial learning rate
in the Adam algorithm since the model has converged in the previous training [23]. It can
guarantee that the ﬁnal model has better generalization ability for the target domain.
Learned Features
0.862
0.148
γ‘
γ
U-net
Pre-trained U-net
For every pixels
0.5 nc6k0.5 nc6k
0.5 0.7 0.1
0.8 0.4 0.2
0.4 0.2 0.8
Fine-tune
Train
0.5 nc6k
0.5 nc6k
RI RI RI
RI RI RI
RI RI RI
Transfer 
parameters
0.5 nc6k0.5 nc6k0.5 nc6k
0.5 0.7 0.1
0.8 0.4 0.2
0.4 0.2 0.8
…
0.5 nc6k
0.5 nc6k0.5 nc6k
0.5 0.7 0.1
0.8 0.4 0.2
0.4 0.2 0.8
kernel weights
…
0.5 nc6k
0.5 nc6k0.5 nc6k0.4 0.6 0.2
0.9 0.4 0.2
0.4 0.2 0.9
Adjust new data distribution
512x512512x512
Classification
0.725
0.275
γ‘
γ
W-900 148 images
W-1000 few images
Predict results
Predict results
max pool 2x2
up-conv 2x2
Concatenate
Concatenate
Concatenate
Concatenate
Concatenate
32
64
128
256
512
1024
512
256
128
64
32
conv 1x1 Sigmoidconv 3x3 Relu +conv 3x3 Relu
Figure 2. The schematic ﬂowchart of deep transfer learning method from W-900 to W-1000, wherein
the U-Net architecture is employed as the basic network.
In the proposed deep transfer learning method, we employ the U-Net encoder-decoder ar-
chitecture as the basic network due to its remarkable simplicity , efficiency , androbustness [24].
In the encoder (feature extraction branches), the image features are extracted using multiple
2D convolutional and pooling layers. These features are transferred to the decoder branch
using the skip connection. Multiple skip connections at different encoder layers transfer
the layer feature maps to the corresponding decoder layer. The decoder contains multiple
decoding convolutional layers and up-sampling layers, and concatenates the transferred
encoding feature maps with the up-sampled feature maps. The last layer of the decoder
contains a softmax activation function, which generates the microstructure recognition on
γ′ phase. Finally , the categorical cross entropy is adopted as the loss function. A detailed
overview of the parameters in the network is also presented in Figure 2.
4. Experimental Results
To show the superiority of deep transfer learning, we conduct two kinds of transfer
learning experiments including transfer from W-900 to W-1000 and transfer from W-1000
to W-900. Wherein each experiment contains different numbers of labeled images from

## Page 5

Materials 2022, 15, 4251 5 of 10
the target domain and full labeled images from the source domain. For comparison, direct
training with random initialization is also performed on W-900 and W-1000, respectively.
4.1. Evaluation Metric
In this paper, three commonly used metrics including Dice-coefﬁcient, Accuracy, and
Intersection over Union (IoU) are adopted for evaluation.
Dice-coefﬁcient is a statistic used to gauge the similarity of two sets, which is deﬁned
as follows:
Dice(T, P) = 2|T∩ P|/(|T| +|P|), (1)
where T means the labeled γ′ phase and P is the predicted γ′ phase.
Accuracy represents the ratio of each positive pixel and negative pixel to be correctly
classiﬁed. The deﬁnition is given as follows:
Accuracy(T, P) = ( TP + TN )/(|T| +|P|), (2)
where TP means the true positive and TN means the true negative.
IoU is deﬁned as the size of the intersection divided by the size of the union of two
sets, which is provided as follows:
IoU(T, P) =|T∩ P|/(|T|∪| P|). (3)
4.2. Recognition Performance
To quantify the performance, the targeted dataset was randomly split into train set, val-
idation set, and test set (60%, 20%, and 20%), respectively. In each experiment, we randomly
select n (n chooses 3, 4, 5, 6, 7, 8) labeled images from the train set to train the classiﬁer,
and the best-performing classiﬁer is determined by minimizing the corresponding soft dice
loss on the validation set [25]. To eliminate the randomness, we repeat 20 times for each
experiment. The average Dice-coefﬁcient, Accuracy, and IoU on the test set are reported in
Table 2. We can see that the Dice-coefﬁcient of deep transfer learning outperforms random
initialization signiﬁcantly, especially when n is smaller. This phenomenon is consistent
with a previous conclusion [26]. It should be noted that deep transfer learning with n = 3
can achieve high recognition performance during the transfer from W-900 to W-1000, where
the average Dice-coefﬁcient is signiﬁcantly improved by about 30% compared with random
initialization. Meanwhile, deep transfer learning with n = 5 can achieve high recognition
performance during the transfer from W-1000 to W-900 and has an improvement up to 7%
on Dice-coefﬁcient than the random initialization.
To have a visual comparison, Figure 3a,b present the box plots of the Dice-coefﬁcient
of two methods at different sample numbers, which is able to show the distribution of
these 20 times experimental results comprehensively. In these ﬁgures, we can clearly
observe the statistical characteristics of experimental results, including upper extreme,
upper quartile, median, lower quartile, and lower extreme. It can be seen that as the number
of labeled images n increases, the Dice-coefﬁcient of random initialization has a more rapid
improvement than that of deep transfer learning. It also supports that deep transfer learning
can achieve excellent performance when there are only a few labeled images. Meanwhile,
we can see that the variance of deep transfer learning is generally smaller than that of
random initialization, especially during the transfer from W-900 to W-1000. It means that
the deep transfer learning is more robust than the random initialization. Figure 3c visually
presents the microstructure recognition performance on γ′ phase. Wherein the green part
represents the TP, the red part represents the false negative (FN), the blue part represents
the false positive ( FP) and the black part represents the TN . We can see that random
initialization tends to produce FN when n is small. In contrast, deep transfer learning can
generally produce TP with a little pixel-level FP and FN. It may owe to the pre-trained
process in the deep transfer learning.

## Page 6

Materials 2022, 15, 4251 6 of 10
Table 2. Average results of deep transfer learning (TL) and random initialization (RI).
Samples Method W-900 to W-1000 W-1000 to W-900
Accuracy Dice IoU Accuracy Dice IoU
3 RI 80.56% 49.48% 36.46% 80.50% 66.00% 52.34%
TL 92.03% 80.68% 69.05% 91.76% 75.53% 62.73%
4 RI 83.05% 60.79% 45.46% 82.70% 66.44% 52.29%
TL 92.00% 80.29% 68.64% 91.87% 75.53% 62.97%
5 RI 89.06% 72.96% 61.02% 82.07% 69.37% 56.71%
TL 92.09% 80.68% 69.24% 91.97% 76.87% 64.74%
6 RI 87.85% 73.88% 60.84% 86.31% 71.39% 58.76%
TL 92.25% 81.37% 70.18% 91.66% 77.05% 65.07%
7 RI 87.37% 73.28% 60.28% 87.81% 72.01% 59.73%
TL 92.15% 81.37% 70.26% 91.90% 77.32% 65.36%
8 RI 90.57% 79.69% 68.61% 89.19% 74.89% 63.63%
TL 92.15% 81.98% 70.78% 91.93% 77.38% 65.33%
SEM images
Random 
Initialization
Transfer 
Learning
3 images 4 images 5 images 6 images 7 images 8 images
(a) (b)
(c)
Ground truth
(d) (e)
Figure 3. (a) The box plot of Dice-coefﬁcient of two methods during the transfer from W-900 to
W-1000; (b) The box plot during the transfer from W-1000 to W-900; (c) Visualization of recognition
results; (d) The validation accuracy vs. different epochs of two methods during the transfer from
W-900 to W-1000; (e) The validation accuracy during the transfer from W-1000 to W-900.

## Page 7

Materials 2022, 15, 4251 7 of 10
4.3. Convergence Speed
Note that another advantage of deep transfer learning is the fast convergence [27]. We
compare the validation accuracy vs. different epochs of deep transfer learning and random
initialization with n = 6. The validation accuracy on transfer from W-900 to W-1000 and
transfer from W-1000 to W-900 are shown in Figure 3d and e, respectively. We can see that
deep transfer learning not only can achieve a classiﬁer with good performance quickly, but is
also superior to the random initialization on validation accuracy. To be speciﬁc, ﬁve epochs
are enough for deep transfer learning to obtain a classiﬁer with satisfying generalization
ability. In contrast, random initialization needs 10 more epochs for convergence. It means
that deep transfer learning helps reduce the training time on γ′ phase recognition. This
phenomenon is also similar with a previous conclusion [26].
4.4. Discussion
This present research is primarily motivated by the fact that the deep-learning-based
image analysis suffers from generalization when the data distribution changes. It means that
the manual annotation will be required to train a new model when facing a similar dataset.
To overcome this problem, the deep transfer learning method is proposed. It aims to take
full advantage of the existing labeled dataset and achieve excellent recognition performance
with a few labeled images for a similar dataset. As expected, the deep transfer learning
method can shorten the training time and achieve satisfying performance with a few labeled
samples. In essence, the deep transfer learning method is equivalent to narrowing the function
hypothesis space based on the prior knowledge learned on existing labeled dataset [28], which
guarantees the accurate and fast recognition on γ′ phase. Although the success of deep
transfer learning method is only validated on two Ni-base superalloys produced at 900◦C and
1000◦C, it also holds great promise that the proposed method can be applied to theγ′ phase
recognition of Ni-base superalloys dataset produced at other temperatures such as800◦C or
other multicomponent superalloys dataset such as Al-based.
5. Software
To facilitate the Ni-based superalloys microstructure recognition, we have developed
and designed a simple software by PyQt Designer [29]. As shown in Figure 4, the overall
software interface mainly contains the user input (left part) and real time monitoring
(right part). The left part includes the common settings during the deep transfer learning
experiment, such as the path of the source domain, the path of the target domain, the choice
of network architecture of basic model, the choice of optimizer, the initial learning rate, the
number of training epochs, and the use of data augmentation. The deep transfer learning
model will start training after the button “run” is pressed. In the upper right window,
the model loss and accuracy vs. different epochs are visualized and updated in real time.
Meanwhile, the progress bar of the whole training is also presented in the lower right
window. In general, the developed software can conduct deep transfer learning experiment
through simple operation for the user.

## Page 8

Materials 2022, 15, 4251 8 of 10
Figure 4. Software interface of deep transfer learning.
6. Conclusions
In this paper, we have proposed a deep transfer learning method for microstructure recog-
nition on γ′ phase, which could use fewer labeled samples to achieve satisfying performance
for a new Ni-based superalloys dataset. To evaluate the effectiveness of the proposed method,
we have produced and annotated two Ni-based superalloys datasets at temperatures 900◦C
and 1000◦C, respectively . The experimental results have showed that the proposed method
only needs five (or less) labeled images to achieve state-of-the-art segmentation accuracy
while enjoying the advantage of fast convergence. Finally , we have developed a simple and
effective software for the Ni-based superalloys microstructure recognition onγ′ phase, which
can facilitate the process of materials characterization and analysis.
Despite the good results, the proposed method still has several shortcomings that can
be improved, such as improving the recognition performance or using fewer labeled images.
Thus, several open problems deserve further research along the line of the present work.
For example, inspired by the success of semi-supervised learning [30,31], how to utilize the
unlabeled images in the target domain is a possible solution to improve the recognition
performance. Similarly, inspired by the image-to-image translation [32], how to generate
the annotated dataset using an existing dataset is a potential solution for unsupervised
microstructure recognition. We are currently researching these problems.
Author Contributions: All authors have made a great contribution to the work. Methodology, W.L.
(Wenyi Li), W.L. (Weifu Li) and C.X.; software, W.L. (Wenyi Li); validation, W.L. (Wenyi Li), W.L.
(Weifu Li); formal analysis, W.L. (Wenyi Li), W.L. (Weifu Li) and C.X.; investigation, W.L. (Wenyi Li)
Z.Q. and C.X.; resources, Z.Q., L.H. and F.L.; data curation, W.L. (Wenyi Li); writing—original draft
preparation, W.L. (Wenyi Li), L.H. and W.L. (Weifu Li); writing—review and editing, W.L. (Weifu Li),
C.X. and L.T.; visualization, W.L. (Wenyi Li); supervision, C.X.; project administration, W.L. (Weifu
Li); funding acquisition, C.X. and F.L. All authors have read and agreed to the published version of
the manuscript.
Funding: This research was funded by the National Science and Technology Major Project (J2019-IV-
0003-0070), the Scientiﬁc Research Foundation of Hainan University (KYQD(ZR)20010), the Funda-
mental Research Funds for the Central Universities of China (2662020LXQD002), the Key Laboratory
of Biomedical Engineering of Hainan Province (Opening Foundation 2022003), the Hubei Key Labora-
tory of Applied Mathematics (Opening Foundation HBAM 202004), the Natural Science Foundation
of China (91860105, 52074366), the China Postdoctoral Science Foundation (2019M662799), the Natu-
ral Science Foundation of Hunan Province of China (2021JJ40757), and the Science and Technology
Innovation Program of Hunan Province (2021RC3131).

## Page 9

Materials 2022, 15, 4251 9 of 10
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1. Pollock, T.M. Alloy design for aircraft engines. Nat. Mater. 2016, 15, 809–815. [CrossRef] [PubMed]
2. Pollock, T.M.; Tin, S. Nickel-based superalloys for advanced turbine engines: chemistry, microstructure and properties. J. Propuls.
Power 2006, 22, 361–374. [CrossRef]
3. Gaag, T.; Ritter, N.; Peters, A.; Volz, N.; Gruber, D.; Neumeier, S.; Zenk, C.; Körner, C. Improving the Effectiveness of the
Solid-Solution-Strengthening Elements Mo, Re, Ru and W in Single-Crystalline Nickel-Based Superalloys. Metals 2021, 11, 1707.
[CrossRef]
4. Wittenzellner, T.; Sumarli, S.; Schaar, H.; Wang, F.; Ma, D.; Bührig-Polaczek, A. Microstructural Investigations of Ni-Based
Superalloys by Directional Solidiﬁcation Quenching Technique. Materials 2020, 13, 4265. [CrossRef]
5. Utada, S.; Despres, L.; Cormier, J. Ultra-High Temperature Creep of Ni-Based SX Superalloys at 1250°C. Metals 2021, 11, 1610.
[CrossRef]
6. Despres, L.; Costil, S.; Cormier, J.; Villechaise, P .; Cariou, R. Impact of Laser Texturing on Ni-Based Single Crystal Superalloys.
Metals 2021, 11, 1737. [CrossRef]
7. Reed, R.C.; Tao, T.; Warnken, N. Alloys-by-design: Application to nickel-based single crystal superalloys. Acta Mater.
2009, 57, 5898–5913. [CrossRef]
8. Liu, F.; Xiao, X.; Huang, L.; Tan, L.; Liu, Y. Design of NiCoCrAl eutectic high entropy alloys by combining machine learning with
CALPHAD method. Mater. T oday Commun.2022, 30, 103172. [CrossRef]
9. Wang, Z.; Zhang, L.; Li, W.; Qin, Z.; Wang, Z.; Li, Z.; Tan, L.; Zhu, L.; Liu, F.; Han, H.; et al. A high-throughput approach to
explore the multi-component alloy space: A case study of nickel-based superalloys. J. Alloys Compd. 2021, 858, 158100. [CrossRef]
10. Qin, Z.; Wang, Z.; Wang, Y.; Zhang, L.; Li, W.; Liu, J.; Wang, Z.; Li, Z.; Pan, J.; Zhao, L.; et al. Phase prediction of Ni-base
superalloys via high-throughput experiments and machine learning. Mater. Res. Lett. 2021, 9, 32–40. [CrossRef]
11. Miracle, D.B.; Senkov, O.N. A critical review of high entropy alloys and related concepts. Acta Mater. 2017, 122, 448–511.
[CrossRef]
12. Geddes, B.; Leon, H.; Huang, X. Superalloys: Alloying and Performance ; ASM International: Materials Park, OH, USA, 2010.
13. Sosa, J.M. Development of T ools for 2D and 3D Microstructural Characterization and Their Application to Titanium Alloy Microstructures ;
The Ohio State University: Columbus, OH, USA, 2015.
14. Sudbrack, C.K.; Ziebell, T.D.; Noebe, R.D.; Seidman, D.N. Effects of a tungsten addition on the morphological evolution, spatial
correlations and temporal evolution of a model Ni–Al–Cr superalloy. Acta Mater. 2008, 56, 448–463. [CrossRef]
15. Sosa, J.M.; Huber, D.E.; Welk, B.; Fraser, H.L. Development and application of MIPAR™ : A novel software package for two-and
three-dimensional microstructural characterization. Integr. Mater. Manuf. Innov. 2014, 3, 123–140. [CrossRef]
16. Gola, J.; Britz, D.; Staudt, T.; Winter, M.; Schneider, A.S.; Ludovici, M.; Mücklich, F. Advanced microstructure classiﬁcation by
data mining methods. Comput. Mater. Sci. 2018, 148, 324–335. [CrossRef]
17. Kondo, R.; Yamakawa, S.; Masuoka, Y.; Tajima, S.; Asahi, R. Microstructure recognition using convolutional neural networks for
prediction of ionic conductivity in ceramics. Acta Mater. 2017, 141, 29–38. [CrossRef]
18. Jia, K.; Li, W.; Wang, Z.; Qin, Z. Accelerating Microstructure Recognition of Nickel-Based Superalloy Data by UNet++.
In Proceedings of the International Conference on Intelligent Automation and Soft Computing, Nanjing, China, 25–27 June 2021;
Springer: Berlin/Heidelberg, Germany, 2021; pp. 863–870.
19. Pan, S.J.; Yang, Q. A survey on transfer learning. IEEE T rans. Knowl. Data Eng. 2009, 22, 1345–1359. [CrossRef]
20. Karimi, D.; Warﬁeld, S.K.; Gholipour, A. Transfer learning in medical image segmentation: New insights from analysis of the
dynamics of model parameters and learned representations. Artif. Intell. Med. 2021, 116, 102078. [CrossRef]
21. Wang, Z.; Zhang, L.; Li, W.; Qin, Z.; Wang, Z.; Li, Z.; Tan, L.; Zhu, L.; Liu, F.; Han, H.; et al. High throughput experiment assisted
discovery of new Ni-base superalloys. Scr. Mater. 2020, 178, 134–138. [CrossRef]
22. Yosinski, J.; Clune, J.; Bengio, Y.; Lipson, H. How transferable are features in deep neural networks? Adv. Neural Inf. Process. Syst.
2014, 27.
23. Tajbakhsh, N.; Shin, J.Y.; Gurudu, S.R.; Hurst, R.T.; Kendall, C.B.; Gotway, M.B.; Liang, J. Convolutional neural networks for
medical image analysis: Full training or ﬁne tuning? IEEE T rans. Med. Imaging 2016, 35, 1299–1312. [CrossRef]
24. Ronneberger, O.; Fischer, P .; Brox, T. U-net: Convolutional networks for biomedical image segmentation. In Proceedings of the
International Conference on Medical Image Computing and Computer-Assisted Intervention, Munich, Germany, 5–9 October
2015; Springer: Berlin/Heidelberg, Germany, 2015; pp. 234–241.
25. Bertels, J.; Eelbode, T.; Berman, M.; Vandermeulen, D.; Maes, F.; Bisschops, R.; Blaschko, M.B. Optimizing the dice score and
jaccard index for medical image segmentation: Theory and practice. In Proceedings of the International Conference on Medical
Image Computing and Computer-Assisted Intervention, Shenzhen, China, 13–17 October 2019; Springer: Berlin/Heidelberg,
Germany, 2019; pp. 92–100.

## Page 10

Materials 2022, 15, 4251 10 of 10
26. Zhuang, F.; Qi, Z.; Duan, K.; Xi, D.; Zhu, Y.; Zhu, H.; Xiong, H.; He, Q. A comprehensive survey on transfer learning. Proc. IEEE
2020, 109, 43–76. [CrossRef]
27. Torrey, L.; Shavlik, J. Transfer learning. In Handbook of Research on Machine Learning Applications and T rends: Algorithms, Methods,
and T echniques; IGI Global: Hershey, PA, USA, 2010; pp. 242–264.
28. Wang, X.; Shen, C.; Xia, M.; Wang, D.; Zhu, J.; Zhu, Z. Multi-scale deep intra-class transfer learning for bearing fault diagnosis.
Reliab. Eng. Syst. Saf. 2020, 202, 107050. [CrossRef]
29. Meier, B. Python GUI Programming Cookbook: Develop Functional and Responsive User Interfaces with Tkinter and PyQt5 ; Packt
Publishing Ltd.: Birmingham, UK, 2019.
30. Chen, D.; Sun, D.; Fu, J.; Liu, S. Semi-supervised learning framework for aluminum alloy metallographic image segmentation.
IEEE Access 2021, 9, 30858–30867. [CrossRef]
31. You, X.; Peng, Q.; Yuan, Y.; Cheung, Y.M.; Lei, J. Segmentation of retinal blood vessels using the radial projection and semi-
supervised approach. Pattern Recognit. 2011, 44, 2314–2324. [CrossRef]
32. Richardson, E.; Alaluf, Y.; Patashnik, O.; Nitzan, Y.; Azar, Y.; Shapiro, S.; Cohen-Or, D. Encoding in Style: A StyleGAN Encoder
for Image-to-Image Translation. In Proceedings of the 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition
(CVPR), Virtual, 19–25 June 2021; pp. 2287–2296.
