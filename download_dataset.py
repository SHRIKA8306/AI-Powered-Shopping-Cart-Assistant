import os
import shutil

def prepare_dataset():
    """
    Prepares the shopping-trolley dataset from local GitHub repo.
    Ensures YOLOv8 expected structure: train/val/test + data.yaml
    """

    base_path = os.path.join(os.getcwd(), "shopping-trolley-5")  # dataset folder in repo
    target_path = os.path.join(os.getcwd(), "datasets", "shopping-trolley-5")

    # Create datasets directory if not exists
    os.makedirs(os.path.join(os.getcwd(), "datasets"), exist_ok=True)

    if os.path.exists(base_path):
        print(f"[INFO] Found dataset in: {base_path}")
        if os.path.exists(target_path):
            print("[INFO] Removing old dataset copy...")
            shutil.rmtree(target_path)

        print("[INFO] Copying dataset to working directory...")
        shutil.copytree(base_path, target_path)
        print(f"[INFO] Dataset ready at: {target_path}")

        # Check structure
        expected = ["train", "valid", "data.yaml"]
        for e in expected:
            path_check = os.path.join(target_path, e)
            if not os.path.exists(path_check):
                print(f"[WARNING] Missing {e} inside dataset folder!")

    else:
        print("[ERROR] Dataset folder 'shopping-trolley-5' not found in repo!")

if __name__ == "__main__":
    prepare_dataset()




