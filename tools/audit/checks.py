import warnings, numpy as np, pandas as pd, sys
warnings.filterwarnings("ignore")
D = sys.argv[1]
print("== C1 graph notebook time parsing (pandas", pd.__version__, ")")
s = pd.Series([1630, 755, 600]).astype(str)
out = s.str.replace(r'(\d{2}$)', '') + ':' + s.str.extract(r'(\d{2}$)', expand=False) + ':00'
print("   produced:", list(out), "| intended: ['16:30:00','7:55:00','6:00:00']")

print("== C2 AirQualityUCI missing-value code -200 in smoothing lesson")
d = pd.read_csv(f"{D}/drive/MyDrive/Colab Notebooks/ExampleData/AirQualityUCI.csv", sep=";", decimal=",").iloc[:, 0:14].dropna()
T = d["T"]; Tc = T.replace(-200, np.nan)
ema_bad = T.ewm(span=40, adjust=False).mean(); ema_ok = Tc.ewm(span=40, adjust=False, ignore_na=True).mean()
print(f"   rows={len(T)} T==-200: {(T==-200).sum()}  min T as taught={T.min()}  min EMA as taught={ema_bad.min():.1f}  min EMA with -200->NaN={ema_ok.min():.1f}")
print(f"   max |EMA difference| = {(ema_bad-ema_ok).abs().max():.1f} degC")

print("== C3 Titanic midterm key: rows kept by df.dropna() and test-set uncertainty")
t = pd.read_csv(f"{D}/train.csv"); n_keep = len(t.dropna()); n_test = int(np.ceil(n_keep/7))
from scipy.stats import binomtest
k = round(0.7777777777777778*n_test)
ci = binomtest(k, n_test).proportion_ci(method="wilson")
print(f"   kept {n_keep}/891 rows; test n={n_test}; accuracy {k}/{n_test}={k/n_test:.3f}; 95% Wilson CI [{ci.low:.2f}, {ci.high:.2f}]")
print(f"   majority-class baseline on kept rows: {max(t.dropna().Survived.mean(),1-t.dropna().Survived.mean()):.3f}")

print("== C4 PCAinAction: eig vs eigh and projection of uncentred data")
from sklearn.datasets import load_iris
X = load_iris().data[:, 2:4]; Xc = X - X.mean(0); C = np.cov(Xc.T)
w, V = np.linalg.eig(C); w2, V2 = np.linalg.eigh(C)
print("   eig order:", np.round(w, 5), "| eigh (ascending):", np.round(w2, 5))
p_uncentred = X @ V[:, 0]; p_centred = Xc @ V[:, 0]
print(f"   mean of projection as taught={p_uncentred.mean():.3f}; centred={p_centred.mean():.3f} (offset only; variance equal: {np.isclose(p_uncentred.var(), p_centred.var())})")

print("== C5 Supervised LDA fitted before split (pattern in FeatureExtraction) on pure noise")
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
rng = np.random.default_rng(0); Xn = rng.normal(size=(200, 150)); yn = rng.integers(0, 2, 200)
Z = LDA(n_components=1).fit(Xn, yn).transform(Xn)
a, b, c, e = train_test_split(Z, yn, test_size=0.3, random_state=101)
leak = RandomForestClassifier(random_state=0).fit(a, c).score(b, e)
ok = cross_val_score(make_pipeline(LDA(n_components=1), RandomForestClassifier(random_state=0)), Xn, yn, cv=5).mean()
print(f"   labels are random (true accuracy 0.5): leaked LDA-then-split test acc={leak:.2f}; LDA inside CV pipeline acc={ok:.2f}")

print("== C6 Mushroom: same comparison on the course dataset")
m = pd.read_csv(f"{D}/mushrooms.csv"); Xm = pd.get_dummies(m.drop(columns="class")).astype(float).values; ym = (m["class"]=="p").astype(int).values
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
print("   majority baseline:", round(cross_val_score(DummyClassifier(), Xm, ym, cv=5).mean(), 3),
      "| depth-2 tree on raw one-hot:", round(cross_val_score(DecisionTreeClassifier(max_depth=2, random_state=0), Xm, ym, cv=5).mean(), 3),
      "| LDA(1)+RF in pipeline:", round(cross_val_score(make_pipeline(LDA(n_components=1), RandomForestClassifier(n_estimators=100, random_state=0)), Xm, ym, cv=5).mean(), 3))
print("   'odor' alone (one-hot) depth-3 tree:", round(cross_val_score(DecisionTreeClassifier(max_depth=3, random_state=0), pd.get_dummies(m[["odor"]]).values, ym, cv=5).mean(), 3))

print("== C7 Dimensionality Reductions: 'regression' tree importances use classification X,y")
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeRegressor
Xc_, yc_ = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, random_state=1)
print("   target values seen by the 'regression' model:", np.unique(yc_))

print("== C8 Final exam Q1 data A=(2,3,5,7,60)")
from scipy.stats import hmean, gmean
A = [2,3,5,7,60]; print(f"   AM={np.mean(A):.3f} GM={gmean(A):.3f} HM={hmean(A):.3f}")
